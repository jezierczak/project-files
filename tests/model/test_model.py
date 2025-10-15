from decimal import Decimal
from src.model import (
    Product,
    Customer,
    Order,
    ProductCategory,
    ShippingMethod,
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict
)
import pytest


def test_product_to_dict(product_1: Product, product_1_data: ProductDataDict) -> None:
    data = product_1.to_dict()
    assert data == product_1_data


def test_customer_to_dict(customer_1: Customer, customer_1_data: CustomerDataDict) -> None:
    data = customer_1.to_dict()
    assert data == customer_1_data


def test_order_to_dict(order_1: Order, order_1_data: OrderDataDict) -> None:
    data = order_1.to_dict()
    assert data == order_1_data
