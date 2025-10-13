from src.validator import Validator
from src.model import ProductCategory, ShippingMethod
from decimal import Decimal

def main() -> None:
    pass

    # products = [
    #     {"id": 1, "name": "PA", "category": "Electronics", "price": "1500"},
    #     {"id": 2, "name": "PB", "category": "Electronics", "price": "1600"}
    # ]
    # product_json_file_writer = ProductJsonFileWriter()
    # product_json_file_writer.write('temp_products.json', products)
    #
    # customers = [
    #     {"id": 1, "first_name": "CA", "last_name": "CCA", "age": 30, "email": "ca@example.com"},
    #     {"id": 2, "first_name": "CB", "last_name": "CCB", "age": 40, "email": "cb@example.com"}
    # ]
    # customer_json_file_writer = CustomerJsonFileWriter()
    # customer_json_file_writer.write('temp_customers.json', customers)
    #
    # orders = [
    #     {"id": 1, "customer_id": 1, "product_id": 1, "quantity": 1, "discount": "0.10", "shipping_method": "Standard"},
    #     {"id": 1, "customer_id": 2, "product_id": 2, "quantity": 2, "discount": "0.20", "shipping_method": "Express"},
    # ]
    # order_json_file_writer = OrderJsonFileWriter()
    # order_json_file_writer.write('temp_orders.json', orders)

    # print(Validator.validate_string_with_regex('ALA', r'[A-Z]+'))
    # print(Validator.validate_string_with_regex('ALa', r'[A-Z]+'))


if __name__ == '__main__':
    main()
