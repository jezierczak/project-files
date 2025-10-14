import logging
import re
from abc import ABC
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Type, override
from email_validator import validate_email, EmailNotValidError
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict

logging.basicConfig(level=logging.INFO)


@dataclass
class AbstractValidator[T](ABC):
    required_keys: list[str] = field(default_factory=list)

    def validate(self, data: T) -> bool:
        return len(self.required_keys) == 0 or self.has_required_keys(data, self.required_keys)

    def has_required_keys(self, data: T, keys: list[str]) -> bool:
        missing_keys = []
        for key in keys:
            if isinstance(data, dict):
                if key not in data:
                    missing_keys.append(key)
            elif not hasattr(data, key):
                missing_keys.append(key)
        if missing_keys:
            logging.error(f"Missing required keys: {missing_keys}")
            return False
        return True

    @staticmethod
    def is_positive(data: int | str) -> bool:
        match data:
            case int(value) if value > 0:
                return True
            case str(value):
                try:
                    decimal_value = Decimal(value)
                    return decimal_value > 0
                except InvalidOperation as e:
                    logging.error(str(e))
                    return False
            case _:
                return False

    @staticmethod
    def is_valid_value_of(value: str, enum_class: Type[Enum]) -> bool:
        return value in [item.value for item in enum_class]

    @staticmethod
    def is_valid_email(email: str) -> bool:
        try:
            validate_email(email, check_deliverability=True)
            return True
        except EmailNotValidError as e:
            logging.error(str(e))
            return False

    @staticmethod
    def validate_int_in_range(value: int, min_value: int, max_value: int) -> bool:
        return min_value <= value <= max_value

    @staticmethod
    def validate_decimal_in_range(value: str, min_value: Decimal, max_value: Decimal) -> bool:
        try:
            decimal_value = Decimal(value)
            return min_value <= decimal_value <= max_value
        except (InvalidOperation, ValueError) as e:
            logging.error(str(e))
            return False

    @staticmethod
    def validate_string_with_regex(value: str, pattern: str) -> bool:
        return re.fullmatch(pattern, value) is not None

@dataclass
class ProductDataDictValidator(AbstractValidator[ProductDataDict]):

    def __post_init__(self):
        if len(self.required_keys) == 0:
            self.required_keys = ['id', 'name', 'category', 'price']

    @override
    def validate(self, data: ProductDataDict) -> bool:
        return super().validate(data) and AbstractValidator.is_positive(data['price'])

@dataclass
class CustomerDataDictValidator(AbstractValidator[CustomerDataDict]):
    min_age: int = 18
    max_age: int = 65

    def __post_init__(self):
        if len(self.required_keys) == 0:
            self.required_keys = ['id', 'first_name', 'last_name', 'age', 'email']

    @override
    def validate(self, data: CustomerDataDict) -> bool:
        return super().validate(data) and AbstractValidator.validate_int_in_range(int(data['age']), self.min_age,
                                                                                  self.max_age)

@dataclass
class OrderDataDictValidator(AbstractValidator[OrderDataDict]):
    min_discount: Decimal = Decimal("0.0")
    max_discount: Decimal = Decimal("1.0")

    def __post_init__(self):
        if len(self.required_keys) == 0:
            self.required_keys = ['id', 'customer_id', 'product_id', 'quantity', 'discount', 'shipping_method']

    @override
    def validate(self, data: OrderDataDict) -> bool:
        return super().validate(data) and AbstractValidator.validate_decimal_in_range(str(data['discount']),
                                                                                      self.min_discount,
                                                                                      self.max_discount)
