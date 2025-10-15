from unittest.mock import MagicMock
from src.repository import ProductDataRepository, CustomerDataRepository, OrderDataRepository
import pytest

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