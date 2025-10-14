from dataclasses import dataclass, field
from collections import defaultdict
from abc import ABC
from src.file_service import AbstractFileReader
from src.validator import AbstractValidator
from src.converter import Converter
from src.model import (
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict,
    Product,
    Customer,
    Order
)
import logging

logging.basicConfig(level=logging.INFO)

CustomersWithPurchasedProducts = dict[Customer, dict[Product, int]]

@dataclass
class AbstractDataRepository[T, U](ABC):
    file_reader: AbstractFileReader[T]
    validator: AbstractValidator[T]
    converter: Converter[T, U]
    filename: str | None = None
    _data: list[U] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.filename is None:
            raise ValueError("No filename set")
        self.refresh_data(self.filename)

    def get_data(self) -> list[U]:
        if not self._data:
            logging.warning("No data available in cache")
        return self._data

    def refresh_data(self, filename: str | None = None) -> list[U]:
        if filename is None:
            logging.warning("No filename provided, using default filename")
        else:
            self.filename = filename

        logging.info(f"Refreshing data from {self.filename} ...")
        self._data = self._process_data(str(self.filename))
        return self._data

    def _process_data(self, filename: str) -> list[U]:
        logging.info(f'Reading data from {filename} ...')
        raw_data = self.file_reader.read(filename)
        valid_data = []
        for entry in raw_data:
            if self.validator.validate(entry):
                converted_entry = self.converter.convert(entry)
                valid_data.append(converted_entry)
            else:
                logging.error(f'Invalid entry: {entry}')
        return valid_data


class ProductDataRepository(AbstractDataRepository[ProductDataDict, Product]):
    pass


class CustomerDataRepository(AbstractDataRepository[CustomerDataDict, Customer]):
    pass


class OrderDataRepository(AbstractDataRepository[OrderDataDict, Order]):
    pass


@dataclass
class PurchaseSummaryRepository[C, P, O]:
    customer_repo: AbstractDataRepository[C, Customer]
    product_repo: AbstractDataRepository[P, Product]
    order_repo: AbstractDataRepository[O, Order]
    _purchase_summary: CustomersWithPurchasedProducts = field(default_factory=dict, init=False)

    def purchase_summary(self, force_refresh: bool = False) -> CustomersWithPurchasedProducts:
        if force_refresh or not self._purchase_summary:
            logging.info('Building or refreshing purchase summary from repositories ...')
            self._purchase_summary = self._build_purchase_summary()
        return self._purchase_summary

    def _build_purchase_summary(self) -> CustomersWithPurchasedProducts:
        purchase_summary: CustomersWithPurchasedProducts = defaultdict(lambda: defaultdict(int))

        # Pozyskujemy dane na temat customers oraz products, ale od razu przeksztalcamy je na dict
        customers = {customer.id: customer for customer in self.customer_repo.get_data()}
        products = {product.id: product for product in self.product_repo.get_data()}
        orders = self.order_repo.get_data()

        for order in orders:
            customer = customers.get(order.customer_id)
            product = products.get(order.product_id)
            if customer and product:
                purchase_summary[customer][product] += order.quantity
            else:
                logging.warning(f'Order {order.id} has invalid customer or product reference')

        return dict(purchase_summary)


