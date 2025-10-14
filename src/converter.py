from abc import ABC, abstractmethod
from typing import override
from decimal import Decimal
from src.model import (
    Product,
    Customer,
    Order,
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict,
    ProductCategory,
    ShippingMethod
)


class Converter[T, U](ABC):

    @abstractmethod
    def convert(self, data: T) -> U:
        pass


class ProductConverter(Converter[ProductDataDict, Product]):

    @override
    def convert(self, data: ProductDataDict) -> Product:
        return Product(
            id=int(data["id"]),
            name=str(data["name"]),
            category=ProductCategory(str(data["category"])),
            price=Decimal(data["price"]),
        )

class CustomerConverter(Converter[CustomerDataDict, Customer]):

    @override
    def convert(self, data: CustomerDataDict) -> Customer:
        return Customer(
            id=int(data["id"]),
            first_name=str(data["first_name"]),
            last_name=str(data["last_name"]),
            age=int(data["age"]),
            email=str(data["email"]),
        )

class OrderConverter(Converter[OrderDataDict, Order]):

    @override
    def convert(self, data: OrderDataDict) -> Order:
        return Order(
            id=int(data["id"]),
            customer_id=int(data["customer_id"]),
            product_id=int(data["product_id"]),
            discount=Decimal(data["discount"]),
            quantity=int(data["quantity"]),
            shipping_method=ShippingMethod(str(data["shipping_method"]))
        )