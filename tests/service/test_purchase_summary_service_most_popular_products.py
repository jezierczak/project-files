from decimal import Decimal
from unittest.mock import MagicMock
from src.model import Customer, Product
from src.repository import PurchaseSummaryRepository, CustomersWithPurchasedProducts
from src.service import PurchaseSummaryService
import pytest
import logging
logging.basicConfig(level=logging.DEBUG)


def test_find_most_popular_products_with_no_purchases(
        service: PurchaseSummaryService,
        mock_repository: MagicMock ) -> None:
    mock_repository.purchase_summary.return_value = {}
    result = service.find_most_popular_products()
    assert result == []


def test_find_most_popular_products_with_single_popular_product(
        service: PurchaseSummaryService,
        mock_repository: MagicMock,
        product_1: Product,
        product_2: Product,
        customer_1: Customer,
        customer_2: Customer
) -> None:
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3, product_2: 1},
        customer_2: {product_1: 2, product_2: 2}
    }
    result = service.find_most_popular_products()
    assert len(result) == 1
    assert result == [product_1]


def test_find_most_popular_products_with_multiple_popular_products(
        service: PurchaseSummaryService,
        mock_repository: MagicMock,
        product_1: Product,
        product_2: Product,
        customer_1: Customer,
        customer_2: Customer
) -> None:
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3, product_2: 3},
        customer_2: {product_1: 2, product_2: 2}
    }
    result = service.find_most_popular_products()
    assert len(result) == 2
    assert result == [product_1, product_2]