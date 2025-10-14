from abc import ABC, abstractmethod
from typing import override
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import json


class AbstractFileReader[T](ABC):
    def read(self, filename: str) -> list[T]:
        with open(filename, 'r', encoding='utf8') as file:
            return json.load(file)


class ProductJsonFileReader(AbstractFileReader[ProductDataDict]):
    pass


class CustomerJsonFileReader(AbstractFileReader[CustomerDataDict]):
    pass


class OrderJsonFileReader(AbstractFileReader[OrderDataDict]):
    pass


class AbstractFileWriter[T](ABC):
    def write(self, filename: str, data: list[T]) -> None:
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class ProductJsonFileWriter(AbstractFileWriter[ProductDataDict]):
    pass


class CustomerJsonFileWriter(AbstractFileWriter[CustomerDataDict]):
    pass


class OrderJsonFileWriter(AbstractFileWriter[OrderDataDict]):
    pass
