from src.file_service import (
    ProductJsonFileReader,
    CustomerJsonFileReader,
    OrderJsonFileReader,
    ProductJsonFileWriter,
    CustomerJsonFileWriter,
    OrderJsonFileWriter
)
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
# from py.path import local
import os
import json


def test_read_products(products_file: str, products_data: list[ProductDataDict]) -> None:
    reader = ProductJsonFileReader()
    products = reader.read(products_file)
    assert products == products_data


def test_read_customers(customers_file: str, customers_data: list[CustomerDataDict]) -> None:
    reader = CustomerJsonFileReader()
    customers = reader.read(customers_file)
    assert customers == customers_data


def test_read_orders(orders_file: str, orders_data: list[OrderDataDict]) -> None:
    reader = ProductJsonFileReader()
    orders = reader.read(orders_file)
    assert orders == orders_data


# def test_write_products(tmpdir: local, products_data: list[ProductDataDict]) -> None:
def test_write_products(tmpdir, products_data: list[ProductDataDict]) -> None:
    writer = ProductJsonFileWriter()
    file_path = os.path.join(tmpdir, 'test_products.json')
    writer.write(file_path, products_data)

    with open(file_path, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)

    assert saved_data == products_data
