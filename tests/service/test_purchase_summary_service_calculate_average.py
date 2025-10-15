from decimal import Decimal
from unittest.mock import MagicMock
from src.model import Customer, Product
from src.repository import PurchaseSummaryRepository, CustomersWithPurchasedProducts
from src.service import PurchaseSummaryService
import pytest
import logging
logging.basicConfig(level=logging.DEBUG)

def test_calculate_average_with_no_purchases(
        service: PurchaseSummaryService,
        customer_1: Customer,
        mock_repository: MagicMock) -> None:
    mock_repository.purchase_summary.return_value = {customer_1: {}}
    result = service.calculate_average_spending_per_customer()
    assert result[customer_1] == Decimal("0.0")


def test_calculate_average_with_single_product(
        service: PurchaseSummaryService,
        customer_1: Customer,
        product_1: Product,
        mock_repository: MagicMock) -> None:
    mock_repository.purchase_summary.return_value = {customer_1: {product_1: 1}}
    result = service.calculate_average_spending_per_customer()
    assert result[customer_1] == product_1.price

def test_calculate_average_with_multiple_products(
        service: PurchaseSummaryService,
        customer_1: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    mock_repository.purchase_summary.return_value = {
        customer_1: {
            product_1: 2,
            product_2: 3,
        }
    }
    result = service.calculate_average_spending_per_customer()
    expected_avg_price = (product_1.total_price(2) + product_2.total_price(3)) / 5
    assert result[customer_1] == expected_avg_price