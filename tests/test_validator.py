from typing import Type
from decimal import Decimal
from enum import Enum
from email_validator import EmailNotValidError
from src.validator import Validator, ProductDataDictValidator, CustomerDataDictValidator, OrderDataDictValidator
from src.model import ProductCategory, ProductDataDict, CustomerDataDict, OrderDataDict
import pytest
import re


@pytest.mark.parametrize("value, expected", [
    (5, True),
    (-5, False),
    (0, False),
    ("10.5", True),
    ("-10.5", False),
    ("abc", False),
    ("0", False)
])
def test_is_positive(value: int, expected: bool) -> None:
    assert Validator.is_positive(value) == expected


@pytest.mark.parametrize("value, enum_class, expected", [
    ('Electronics', ProductCategory, True),
    ('Clothing', ProductCategory, True),
    ('Books', ProductCategory, True),
    ('ELECTRONICS', ProductCategory, False),
    ('CLOTHING', ProductCategory, False),
    ('BOOKS', ProductCategory, False),
])
def test_is_valid_value_of(value: str, enum_class: Type[Enum], expected: bool) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected


@pytest.mark.parametrize("email, expected", [
    ("valid@gmail.com", True),  # Poprawny e-mail
    ("valid@example.com", False),  # Domena nie istnieje
    ("invalid-email.com", False),  # Brak @
    ("@missingusername.com", False),  # Brak lokalnej części
    ("missingdomain@", False),  # Brak domeny
    ("user@nonexistentdomain.invalid", False)  # Nieistniejąca domena
])
def test_is_valid_email(email: str, expected: bool) -> None:
    assert Validator.is_valid_email(email) == expected

@pytest.mark.parametrize("value, min_value, max_value, expected", [
    (10, 5, 15, True),
    (4, 5, 10, False),
    (11, 5, 10, False),
    (5, 5, 10, True),
    (10, 5, 10, True),
])
def test_validate_int_in_range(value: int, min_value: int, max_value: int, expected: bool) -> None:
    assert Validator.validate_int_in_range(value, min_value, max_value) == expected

@pytest.mark.parametrize("value, min_value, max_value, expected", [
    ("10.5", Decimal("5.0"), Decimal("15.0"), True),
    ("4.9", Decimal("5.0"), Decimal("15.0"), False),
    ("15.1", Decimal("5.0"), Decimal("15.0"), False),
    ("5.0", Decimal("5.0"), Decimal("15.0"), True),
    ("15.0", Decimal("5.0"), Decimal("15.0"), True),
    ("abc", Decimal("5.0"), Decimal("15.0"), False),
])
def test_validate_decimal_in_range(value: str, min_value: Decimal, max_value: Decimal, expected: bool) -> None:
    assert Validator.validate_decimal_in_range(value, min_value, max_value) == expected

@pytest.mark.parametrize("value, pattern, expected", [
    ("abc123", r'[a-z]+\d+', True),
    ("123abc", r'[a-z]+\d+', False)
])
def test_validate_string_with_regex(value: str, pattern: str, expected: bool) -> None:
    assert Validator.validate_string_with_regex(value, pattern) == expected


@pytest.mark.parametrize("data, expected", [
    ({"id": 1, "name": "A", "category": ProductCategory.BOOKS, "price": 10}, True),
    ({"id": 1, "name": "A", "category": ProductCategory.BOOKS, "price": "15.5"}, True),
    ({"id": 1, "name": "A", "category": ProductCategory.BOOKS, "price": -10}, False),
    ({"id": 1, "name": "A", "category": ProductCategory.BOOKS, "price": "0"}, False),
    ({"id": 1, "name": "A", "category": ProductCategory.BOOKS, "price": "abc"}, False),
    ({"id": 1, "name": "A", "c": ProductCategory.BOOKS, "price": "15.5"}, False),
])
def test_product_data_dict_validator(data: ProductDataDict, expected: bool) -> None:
    validator = ProductDataDictValidator()
    assert validator.validate(data) == expected


@pytest.mark.parametrize("data, min_age, max_age, expected", [
    ({"age": 18}, 18, 65, True),
    ({"age": 65}, 18, 65, True),
    ({"age": 30}, 18, 65, True),
    ({"age": 17}, 18, 65, False),
    ({"age": 66}, 18, 65, False),
])
def test_customer_data_dict_validator(data: CustomerDataDict, min_age: int, max_age: int, expected: bool) -> None:
    validator = CustomerDataDictValidator(min_age, max_age, ["age"])
    assert validator.validate(data) == expected

@pytest.mark.parametrize("data, expected", [
    ({"discount": "0.5"}, True),
    ({"discount": "0.0"}, True),
    ({"discount": "1.0"}, True),
    ({"discount": "-0.5"}, False),
    ({"discount": "1.1"}, False),
    ({"discount": "abc"}, False),
])
def test_order_data_dict_validator(data: OrderDataDict, expected: bool) -> None:
    validator = OrderDataDictValidator(required_keys=["discount"])
    assert validator.validate(data) == expected