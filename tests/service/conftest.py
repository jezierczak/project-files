from unittest.mock import MagicMock
from src.repository import PurchaseSummaryRepository
from src.service import PurchaseSummaryService
import pytest

@pytest.fixture
def mock_repository() -> MagicMock:
    return MagicMock()

@pytest.fixture
def service(mock_repository: MagicMock) -> PurchaseSummaryService:
    return PurchaseSummaryService(repository=mock_repository)
