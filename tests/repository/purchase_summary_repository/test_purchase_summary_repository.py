from unittest.mock import MagicMock
from decimal import Decimal
from src.model import (
    Customer,
    Product,
    Order,
    ProductCategory,
    ShippingMethod,
    CustomerDataDict,
    ProductDataDict,
    OrderDataDict
)
from src.repository import PurchaseSummaryRepository
from typing import cast
import pytest

def test_initial_state_empty_cache(purchase_summary_repo: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]) -> None:
    assert purchase_summary_repo._purchase_summary == {}

def test_purchase_summary_build_cache(
        purchase_summary_repo: PurchaseSummaryRepository,
        product_1: Product,
        product_2: Product,
        customer_1: Customer,
        customer_2: Customer) -> None:
    summary = purchase_summary_repo.purchase_summary()

    assert len(summary) == 2

    cust_1 = summary.get(customer_1)
    assert cust_1 is not None
    assert cust_1[product_1] == 2
    assert cust_1[product_2] == 5

    cust_2 = summary.get(customer_2)
    assert cust_2 is not None
    assert cust_2[product_1] == 1

def test_purchase_summary_cache_reuse(purchase_summary_repo: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]) -> None:
    summary = purchase_summary_repo.purchase_summary()
    assert len(summary) > 0

    customer_repo_mock = cast(MagicMock, purchase_summary_repo.customer_repo.get_data)
    customer_repo_mock.return_value.append(
        Customer(id=3, first_name="Alice", last_name="Smith", age=40, email="alice.smith@example.com")
    )

    summary = purchase_summary_repo.purchase_summary()
    assert len(summary) == 2


def test_purchase_summary_force_refresh(
        purchase_summary_repo: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict],
        customer_1: Customer,
        product_1: Product) -> None:
    _ = purchase_summary_repo.purchase_summary()

    new_order = Order(
        id=4,
        customer_id=1,
        product_id=101,
        quantity=3,
        discount=Decimal("0.05"),
        shipping_method=ShippingMethod.STANDARD
    )

    order_repo_mock = cast(MagicMock, purchase_summary_repo.order_repo.get_data)
    order_repo_mock.return_value.append(new_order)
    summary = purchase_summary_repo.purchase_summary(force_refresh=True)
    assert summary[customer_1][product_1] == 5


def test_invalid_entry_logs_warning(
        purchase_summary_repo: PurchaseSummaryRepository,
        caplog: pytest.LogCaptureFixture) -> None:
    invalid_order = Order(
        id=5,
        customer_id=99,
        product_id=999,
        quantity=1,
        discount=Decimal("0.0"),
        shipping_method=ShippingMethod.STANDARD
    )
    order_repo_mock = cast(MagicMock, purchase_summary_repo.order_repo.get_data)
    order_repo_mock.return_value.append(invalid_order)

    with caplog.at_level("WARNING"):
        _ = purchase_summary_repo.purchase_summary(force_refresh=True)
        assert any("invalid customer or product reference" in record.message for record in caplog.records)
