from unittest.mock import MagicMock
from decimal import Decimal
from src.model import Customer, Product, Order, ProductCategory, ShippingMethod
from src.repository import PurchaseSummaryRepository
import pytest

def test_initial_state_empty_cache(purchase_summary_repo: PurchaseSummaryRepository):
    assert purchase_summary_repo._purchase_summary == {}

def test_purchase_summary_build_cache(
        purchase_summary_repo: PurchaseSummaryRepository,
        product_1: Product,
        product_2: Product,
        customer_1: Customer,
        customer_2: Customer):
    summary = purchase_summary_repo.purchase_summary()

    assert len(summary) == 2

    customer_1 = summary.get(customer_1)
    assert customer_1 is not None
    assert customer_1[product_1] == 2
    assert customer_1[product_2] == 5

    customer_2 = summary.get(customer_2)
    assert customer_2 is not None
    assert customer_2[product_1] == 1