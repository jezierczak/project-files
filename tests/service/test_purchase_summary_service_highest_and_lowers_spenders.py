from decimal import Decimal
from unittest.mock import MagicMock
from src.model import Customer, Product
from src.repository import PurchaseSummaryRepository, CustomersWithPurchasedProducts
from src.service import PurchaseSummaryService
import pytest
import logging
logging.basicConfig(level=logging.DEBUG)


def test_find_highest_and_lowest_spenders_with_no_purchases(
        service: PurchaseSummaryService,
        mock_repository: MagicMock ) -> None:
    mock_repository.purchase_summary.return_value = {}
    highest_spenders, lowest_spenders = service.find_highest_and_lowest_spenders()
    assert highest_spenders == []
    assert lowest_spenders == []

def test_find_highest_and_lowest_spenders_with_different_spending(
        service: PurchaseSummaryService,
        mock_repository: MagicMock,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product
) -> None:
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3},
        customer_2: {product_1: 1},
    }
    highest_spenders, lowest_spenders = service.find_highest_and_lowest_spenders()
    assert highest_spenders == [customer_1]
    assert lowest_spenders == [customer_2]

def test_find_highest_and_lowest_spenders_with_multiple_highest_and_lowest(
        service: PurchaseSummaryService,
        mock_repository: MagicMock,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product
) -> None:
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3},
        customer_2: {product_1: 3},
    }
    highest_spenders, lowest_spenders = service.find_highest_and_lowest_spenders()
    assert highest_spenders == [customer_1, customer_2]
    assert lowest_spenders == [customer_1, customer_2]

