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
    def convert(self, data: T) -> U:  # pragma: no cover
        pass


class ProductConverter(Converter[ProductDataDict, Product]):
    """
    A converter class that transforms data in the format of `ProductDataDict`
    into a `Product` object. Inherits from the generic `Converter` class.
    """

    @override
    def convert(self, data: ProductDataDict) -> Product:
        """
        Converts a `ProductDataDict` dictionary into a `Product` object.

        :param data: The product data dictionary containing fields necessary
                     for creating a `Product` object. Expected keys are:
                     - "id": The unique identifier for the product (string or int).
                     - "name": The name of the product (string).
                     - "category": The category of the product (string, compatible with `ProductCategory`).
                     - "price": The price of the product (string or decimal representation).

        :type data: ProductDataDict
        :return: A `Product` object with values populated from `data`.
        :rtype: Product
        :raises ValueError: If any required field is missing or if the values
                            cannot be converted as expected (e.g., if `id` cannot be converted to int).
        """

        return Product(
            id=data["id"],
            name=data["name"],
            category=ProductCategory(data["category"]),
            price=Decimal(data["price"]),
        )


class CustomerConverter(Converter[CustomerDataDict, Customer]):

    @override
    def convert(self, data: CustomerDataDict) -> Customer:
        return Customer(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            email=data["email"],
        )


class OrderConverter(Converter[OrderDataDict, Order]):

    @override
    def convert(self, data: OrderDataDict) -> Order:
        return Order(
            id=int(data["id"]),
            customer_id=data["customer_id"],
            product_id=data["product_id"],
            discount=Decimal(data["discount"]),
            quantity=data["quantity"],
            shipping_method=ShippingMethod(data["shipping_method"])
        )
