from src.model import ProductDataDict, CustomerDataDict, OrderDataDict, Customer
import pytest
import os
import json


@pytest.fixture
def products_data() -> list[ProductDataDict]:
    return [
        {"id": 1, "name": "PA", "category": "Electronics", "price": "1500"},
        {"id": 2, "name": "PB", "category": "Electronics", "price": "1600"}
    ]

@pytest.fixture
def customers_data() -> list[CustomerDataDict]:
    return [
        {"id": 1, "first_name": "CA", "last_name": "CCA", "age": 30, "email": "ca@example.com"},
        {"id": 2, "first_name": "CB", "last_name": "CCB", "age": 40, "email": "cb@example.com"}
    ]

@pytest.fixture
def orders_data() -> list[OrderDataDict]:
    return [
        {"id": 1, "customer_id": 1, "product_id": 1, "quantity": 1, "discount": "0.10", "shipping_method": "Standard"},
        {"id": 1, "customer_id": 2, "product_id": 2, "quantity": 2, "discount": "0.20", "shipping_method": "Express"},
    ]


# tmpdir: To wbudowana fixture pytest, która tworzy tymczasowy katalog na potrzeby testu. Możesz w nim
# bezpiecznie przechowywać pliki testowe, a po zakończeniu testu katalog i pliki są automatycznie usuwane.

@pytest.fixture
def products_file(tmpdir, products_data) -> str:
    file_path = os.path.join(tmpdir, 'test_products.json')
    with open(file_path, 'w') as file:
        json.dump(products_data, file)
    return file_path

@pytest.fixture
def customers_file(tmpdir, customers_data) -> str:
    file_path = os.path.join(tmpdir, 'test_customers.json')
    with open(file_path, 'w') as file:
        json.dump(customers_data, file)
    return file_path

@pytest.fixture
def orders_file(tmpdir, orders_data) -> str:
    file_path = os.path.join(tmpdir, 'test_orders.json')
    with open(file_path, 'w') as file:
        json.dump(orders_data, file)
    return file_path
