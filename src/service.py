from dataclasses import dataclass
from collections import Counter
from decimal import Decimal
from src.model import Customer, Product
from src.repository import PurchaseSummaryRepository, CustomersWithPurchasedProducts
import logging
logging.basicConfig(level=logging.INFO)


@dataclass(eq=False, frozen=False)
class PurchaseSummaryService:
    repository: PurchaseSummaryRepository

    def calculate_average_spending_per_customer(self) -> dict[Customer, Decimal]:
        average_spending = {}
        for customer, purchases in self.repository.purchase_summary().items():
            total_spent = self.calculate_total_spent(purchases)
            total_items = sum(purchases.values())
            average_spending[customer] = total_spent / Decimal(total_items) if total_items > 0 else Decimal("0.0")
        return average_spending

    def find_most_popular_products(self) -> list[Product]:
        product_counter: Counter[Product] = Counter()

        for purchases in self.repository.purchase_summary().values():
            for product, quantity in purchases.items():
                product_counter[product] += quantity

        if not product_counter:
            return []

        max_count = max(product_counter.values())
        return [product for product, count in product_counter.items() if count == max_count]

    def find_highest_and_lowest_spenders(self) -> tuple[list[Customer], list[Customer]]:
        max_spent = Decimal("-Infinity")
        min_spent = Decimal("Infinity")
        highest_spenders = []
        lowest_spenders = []

        for customer, purchases in self.repository.purchase_summary().items():
            total_spent = self.calculate_total_spent(purchases)

            if total_spent > max_spent:
                max_spent = total_spent
                highest_spenders = [customer]
            elif total_spent == max_spent:
                highest_spenders.append(customer)

            if total_spent < min_spent:
                min_spent = total_spent
                lowest_spenders = [customer]
            elif total_spent == min_spent:
                lowest_spenders.append(customer)

        return highest_spenders, lowest_spenders

    @staticmethod
    def calculate_total_spent(purchases: dict[Product, int]) -> Decimal:
        return sum((product.total_price(quantity) for product, quantity in purchases.items()), Decimal("0.0"))