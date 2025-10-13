import pytest
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


@pytest.mark.parametrize("data, product", [
    (
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": "999.99"},
            Product(id=1, name="Laptop", category=ProductCategory.ELECTRONICS, price=Decimal("999.99"))
    ),
    (
            {"id": 2, "name": "Book", "category": "Books", "price": "19.99"},
            Product(id=2, name="Book", category=ProductCategory.BOOKS, price=Decimal("19.99"))
    ),
])
def test_product_converter_from_json(data: ProductDataDict, product: Product) -> None:
    converter = ProductConverter()
    result = converter.from_json(data)
    assert result.id == product.id
    assert result.name == product.name
    assert result.category == product.category
    assert result.price == product.price


@pytest.mark.parametrize("data, customer", [
    (
            {"id": 1, "first_name": "A", "last_name": "AA", "age": 10, "email": "a@gmail.com"},
            Customer(id=1, first_name= "A", last_name= "AA", age= 10, email= "a@gmail.com")
    ),
    (
            {"id": 2, "first_name": "B", "last_name": "BB", "age": 20, "email": "b@gmail.com"},
            Customer(id=2, first_name= "B", last_name= "BB", age= 20, email= "b@gmail.com")
    ),
])
def test_customer_converter_from_json(data: CustomerDataDict, customer: Customer) -> None:
    converter = CustomerConverter()
    result = converter.from_json(data)
    assert result.id == customer.id
    assert result.first_name == customer.first_name
    assert result.last_name == customer.last_name
    assert result.age == customer.age
    assert result.email == customer.email


@pytest.mark.parametrize("data, order", [
    (
            {"id": 1, "customer_id": 1, "product_id": 1, "discount": "0.1", "quantity": 1, "shipping_method": "Standard"},
            Order(id=1, customer_id= 1, product_id= 1, discount= Decimal("0.1"), quantity= 1, shipping_method= ShippingMethod.STANDARD)
    ),
    (
            {"id": 2, "customer_id": 2, "product_id": 2, "discount": "0.2", "quantity": 2, "shipping_method": "Express"},
            Order(id=2, customer_id= 2, product_id= 2, discount= Decimal("0.2"), quantity= 2, shipping_method= ShippingMethod.EXPRESS)
    ),
])
def test_order_converter_from_json(data: OrderDataDict, order: Order) -> None:
    converter = OrderConverter()
    result = converter.from_json(data)
    assert result.id == order.id
    assert result.customer_id == order.customer_id
    assert result.product_id == order.product_id
    assert result.quantity == order.quantity
    assert result.discount == order.discount
    assert result.shipping_method == order.shipping_method
