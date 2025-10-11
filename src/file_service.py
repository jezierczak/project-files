from abc import ABC, abstractmethod
from typing import override
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import json

class FileReader[T]:
    def read(self, filename: str) -> list[T]:
        with open(filename, 'r', encoding='utf8') as file:
            return json.load(file)

class FileWriter[T](ABC):
    @abstractmethod
    def write(self, filename: str, data: list[T]) -> None:
        pass


class ProductJsonFileReader(FileReader[ProductDataDict]):
    pass

class CustomerJsonFileReader(FileReader[CustomerDataDict]):
    pass

class OrderJsonFileReader(FileReader[OrderDataDict]):
    pass
