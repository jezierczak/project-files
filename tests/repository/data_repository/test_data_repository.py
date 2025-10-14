import pytest
from unittest.mock import MagicMock
from decimal import Decimal
from src.repository import ProductDataRepository, CustomerDataRepository, OrderDataRepository
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict, Product, Customer, Order, ProductCategory
from src.converter import ProductConverter, CustomerConverter, OrderConverter
from src.validator import ProductDataDictValidator, CustomerDataDictValidator, OrderDataDictValidator
from src.file_service import ProductJsonFileReader
from pathlib import Path
import json
import logging


def test_get_data_empty_cache_logs_warning(
        product_data_repository: ProductDataRepository,
        caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.WARNING):
        data = product_data_repository.get_data()
    assert "No data available in cache" in caplog.text
    assert len(data) == 0


def test_refresh_product_data_calls_file_reader_and_process_data(
        product_data_repository: ProductDataRepository, file_reader_mock: MagicMock
) -> None:
    file_reader_mock.read.return_value = [{"id": 1, "name": "Laptop", "category": "Electronics", "price": "999.99"}]
    product_data_repository.validator.validate.return_value = True  # type: ignore[attr-defined]
    product_data_repository.converter.convert.return_value = Product(id=1, name="Laptop", category=ProductCategory.ELECTRONICS, price=Decimal("999.99"))  # type: ignore[attr-defined]

    data = product_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with('products.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert data[0].id == 1
    assert data[0].name == "Laptop"
    assert data[0].category == ProductCategory.ELECTRONICS
    assert data[0].price == Decimal("999.99")


def test_refresh_customer_data_calls_file_reader_and_process_data(
        customer_data_repository: CustomerDataRepository, file_reader_mock: MagicMock
) -> None:
    file_reader_mock.read.return_value = [
        {"id": 1, "first_name": "A", "last_name": "AA", "age": 10, "email": "a@gmail.com"}]
    customer_data_repository.validator.validate.return_value = True  # type: ignore[attr-defined]
    customer_data_repository.converter.convert.return_value = Customer(id=1, first_name="A", last_name="AA", age=10, email="a@gmail.com")  # type: ignore[attr-defined]

    data = customer_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with('customers.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert data[0].id == 1
    assert data[0].first_name == "A"
    assert data[0].last_name == "AA"
    assert data[0].age == 10
    assert data[0].email == "a@gmail.com"

def test_refresh_customer_data_calls_file_reader_and_process_data_2(
        validator_mock: MagicMock,
        converter_mock: MagicMock,
        file_reader_mock: MagicMock
) -> None:
    file_reader_mock.read.return_value = [
        {"id": 1, "first_name": "A", "last_name": "AA", "age": 10, "email": "a@gmail.com"}]
    validator_mock.validate.return_value = True
    converter_mock.convert.return_value \
        = Customer(id=1, first_name="A", last_name="AA", age=10, email="a@gmail.com")

    customer_data_repository = CustomerDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        filename='customers.json'
    )
    data = customer_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with('customers.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert data[0].id == 1
    assert data[0].first_name == "A"
    assert data[0].last_name == "AA"
    assert data[0].age == 10
    assert data[0].email == "a@gmail.com"


def test_invalid_entry_logs_error(
        product_data_repository: ProductDataRepository,
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        caplog: pytest.LogCaptureFixture
) -> None:

    file_reader_mock.read.return_value = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": "999.99"},
        {"id": 2, "name": "Phone", "category": "Electronics"}
    ]

    validator_mock.validate.side_effect = [True, False]

    with caplog.at_level(logging.ERROR):
        data = product_data_repository.refresh_data()

    assert "Invalid entry: {'id': 2, 'name': 'Phone', 'category': 'Electronics'}" in caplog.text
    assert len(data) == 1


def test_no_filename_raises_value_error(
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> None:
    with pytest.raises(ValueError, match='No filename set'):
        product_data_repository = ProductDataRepository(
            file_reader=file_reader_mock,
            validator=validator_mock,
            converter=converter_mock,
            filename=None
        )


