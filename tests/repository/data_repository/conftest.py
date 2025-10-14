import pytest
from unittest.mock import MagicMock, create_autospec
from typing import cast
from src.repository import ProductDataRepository, CustomerDataRepository, OrderDataRepository
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict, Product, Customer, Order
from src.file_service import AbstractFileReader
from src.converter import Converter
import logging
from src.validator import AbstractValidator


@pytest.fixture
def file_reader_mock() -> MagicMock:
    return MagicMock()

@pytest.fixture
def validator_mock() -> MagicMock:
    return MagicMock()

@pytest.fixture
def converter_mock() -> MagicMock:
    return MagicMock()

@pytest.fixture
def product_data_repository(
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> ProductDataRepository:
    return ProductDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        filename='products.json'
    )

@pytest.fixture
def customer_data_repository(
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> CustomerDataRepository:
    return CustomerDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        filename='customers.json'
    )

@pytest.fixture
def order_data_repository(
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> OrderDataRepository:
    return OrderDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        filename='orders.json'
    )