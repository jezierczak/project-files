import pytest
from pytest import FixtureRequest
from src.converter import ProductConverter, CustomerConverter, OrderConverter
from src.model import (
    Product,
    ProductDataDict,
    ProductCategory,
    Customer,
    CustomerDataDict,
    OrderDataDict,
    Order,
    ShippingMethod
)
from decimal import Decimal


@pytest.mark.parametrize("product_data_fixture_name, product_fixture_name", [
    ("product_1_data", "product_1"),
    ("product_2_data", "product_2")
])
def test_product_converter_from_json(
        product_data_fixture_name: str,
        product_fixture_name: str,
        request: FixtureRequest) -> None:
    product = request.getfixturevalue(product_fixture_name)
    product_data = request.getfixturevalue(product_data_fixture_name)
    converter = ProductConverter()
    result = converter.convert(product_data)
    assert result.id == product.id
    assert result.name == product.name
    assert result.category == product.category
    assert result.price == product.price


@pytest.mark.parametrize("customer_data_fixture_name, customer_fixture_name", [
    ("customer_1_data", "customer_1"),
    ("customer_2_data", "customer_2")
])
def test_customer_converter_from_json(
        customer_data_fixture_name: str,
        customer_fixture_name: str,
        request: FixtureRequest) -> None:
    customer = request.getfixturevalue(customer_fixture_name)
    customer_data = request.getfixturevalue(customer_data_fixture_name)
    converter = CustomerConverter()
    result = converter.convert(customer_data)
    assert result.id == customer.id
    assert result.first_name == customer.first_name
    assert result.last_name == customer.last_name
    assert result.age == customer.age
    assert result.email == customer.email


@pytest.mark.parametrize("order_data_fixture_name, order_fixture_name", [
    ("order_1_data", "order_1"),
    ("order_2_data", "order_2"),
])
def test_order_converter_from_json(
        order_data_fixture_name: str,
        order_fixture_name: str,
        request: FixtureRequest) -> None:

    order = request.getfixturevalue(order_fixture_name)
    order_data = request.getfixturevalue(order_data_fixture_name)
    converter = OrderConverter()
    result = converter.convert(order_data)
    assert result.id == order.id
    assert result.customer_id == order.customer_id
    assert result.product_id == order.product_id
    assert result.quantity == order.quantity
    assert result.discount == order.discount
    assert result.shipping_method == order.shipping_method
