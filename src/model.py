from enum import Enum
from dataclasses import dataclass
from decimal import Decimal

ProductDataDict = dict[str, str | int]
CustomerDataDict = dict[str, str | int]
OrderDataDict = dict[str, str | int]

class ProductCategory(Enum):
    ELECTRONICS = 'Electronics'
    CLOTHING = 'Clothing'
    BOOKS = 'Books'


class ShippingMethod(Enum):
    STANDARD = 'Standard'
    EXPRESS = 'Express'


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    category: ProductCategory
    price: Decimal

    def total_price(self, quantity: int) -> Decimal:
        return self.price * quantity

    def to_dict(self) -> ProductDataDict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "price": str(self.price)
        }


@dataclass(frozen=True)
class Customer:
    id: int
    first_name: str
    last_name: str
    age: int
    email: str

    def to_dict(self) -> CustomerDataDict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email
        }

@dataclass
class Order:
    id: int
    customer_id: int
    product_id: int
    quantity: int
    discount: Decimal
    shipping_method: ShippingMethod

    def to_dict(self) -> OrderDataDict:
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "discount": str(self.discount),
            "shipping_method": self.shipping_method.value,
        }