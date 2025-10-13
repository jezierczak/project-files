from abc import ABC, abstractmethod
from typing import override
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import json


class FileReader[T]:
    def read(self, filename: str) -> list[T]:
        with open(filename, 'r', encoding='utf8') as file:
            return json.load(file)


class ProductJsonFileReader(FileReader[ProductDataDict]):
    pass


class CustomerJsonFileReader(FileReader[CustomerDataDict]):
    pass


class OrderJsonFileReader(FileReader[OrderDataDict]):
    pass


class FileWriter[T]:
    def write(self, filename: str, data: list[T]) -> None:
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class ProductJsonFileWriter(FileWriter[ProductDataDict]):
    pass


class CustomerJsonFileWriter(FileWriter[CustomerDataDict]):
    pass


class OrderJsonFileWriter(FileWriter[OrderDataDict]):
    pass
