from decimal import Decimal
from src.model import (
    Product,
    Customer,
    Order,
    ProductCategory,
    ShippingMethod
)
import pytest


def test_product_to_dict(product1: Product):
    data = product1.to_dict()
    expected_data = {
        'id': 1,
        'name': 'Laptop',
        'category': 'Electronics',
        'price': '1500.00'
    }
    assert data == expected_data

def test_customer_to_dict(customer1: Customer):
    data = customer1.to_dict()
    expected_data = {
        'id': 1,
        'first_name': 'Alice',
        'last_name': 'Smith',
        'age': 30,
        'email': 'alice.smith@example.com'
    }
    assert data == expected_data

def test_order_to_dict(order1: Order):
    data = order1.to_dict()
    expected_data = {
        'id': 1,
        'customer_id': 1,
        'product_id': 1,
        'quantity': 1,
        'discount': '0.10',
        'shipping_method': 'Standard'
    }
    assert data == expected_data
