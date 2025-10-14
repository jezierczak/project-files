from decimal import Decimal
from unittest.mock import MagicMock
from src.model import Customer, Product, Order, ProductCategory, ShippingMethod
from src.repository import PurchaseSummaryRepository
import pytest


@pytest.fixture
def customer_1() -> Customer:
    return Customer(id=1, first_name="John", last_name="Doe", age=30, email="john.doe@example.com")


@pytest.fixture
def customer_2() -> Customer:
    return Customer(id=2, first_name="Jane", last_name="Doe", age=25, email="jane.doe@example.com")


@pytest.fixture
def product_1() -> Product:
    return Product(id=101, name="Laptop", category=ProductCategory.ELECTRONICS, price=Decimal("1500.00"))


@pytest.fixture
def product_2() -> Product:
    return Product(id=102, name="T-Shirt", category=ProductCategory.CLOTHING, price=Decimal("20.00"))


@pytest.fixture
def order_1() -> Order:
    return Order(id=1, customer_id=1, product_id=101, quantity=2, discount=Decimal("0.1"),
                 shipping_method=ShippingMethod.STANDARD)


@pytest.fixture
def order_2() -> Order:
    return Order(id=2, customer_id=1, product_id=102, quantity=5, discount=Decimal("0.0"),
                 shipping_method=ShippingMethod.EXPRESS)


@pytest.fixture
def order_3() -> Order:
    return Order(id=3, customer_id=2, product_id=101, quantity=1, discount=Decimal("0.2"),
                 shipping_method=ShippingMethod.STANDARD)


@pytest.fixture
def mock_customer_repo(customer_1: Customer, customer_2: Customer) -> MagicMock:
    repo = MagicMock()
    repo.get_data.return_value = [customer_1, customer_2]
    return repo


@pytest.fixture
def mock_product_repo(product_1: Product, product_2: Product) -> MagicMock:
    repo = MagicMock()
    repo.get_data.return_value = [product_1, product_2]
    return repo


@pytest.fixture
def mock_order_repo(order_1: Order, order_2: Order, order_3: Order) -> MagicMock:
    repo = MagicMock()
    repo.get_data.return_value = [order_1, order_2, order_3]
    return repo


@pytest.fixture
def purchase_summary_repo(
        mock_customer_repo: MagicMock,
        mock_product_repo: MagicMock,
        mock_order_repo: MagicMock) -> PurchaseSummaryRepository:
    return PurchaseSummaryRepository(
        customer_repo=mock_customer_repo,
        product_repo=mock_product_repo,
        order_repo=mock_order_repo
    )
