from src.file_service import (
    ProductJsonFileReader,
    CustomerJsonFileReader,
    OrderJsonFileReader
)

def main() -> None:
    product_json_file_reader = ProductJsonFileReader()
    products = product_json_file_reader.read('./data/products.json')
    for product in products:
        print(product)

    customer_json_file_reader = CustomerJsonFileReader()
    customers = customer_json_file_reader.read('./data/customers.json')
    for customer in customers:
        print(customer)


    order_json_repository = OrderJsonFileReader()
    orders = order_json_repository.read('./data/orders.json')
    for order in orders:
        print(order)


if __name__ == '__main__':
    main()
