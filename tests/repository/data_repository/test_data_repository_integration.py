from decimal import Decimal
import json
from decimal import Decimal
from pathlib import Path
from src.converter import ProductConverter
from src.file_service import ProductJsonFileReader
from src.model import Product, ProductCategory, ProductDataDict
from src.repository import ProductDataRepository
from src.validator import ProductDataDictValidator

"""
W nowych projektach zaleca się używanie tmp_path, ponieważ integruje się z pathlib i jest 
bardziej zgodny ze współczesnymi standardami Pythona. Jeśli jednak pracujesz z kodem, który 
używa py.path.local lub potrzebujesz funkcji dostępnych tylko w tmpdir, warto pozostać przy 
tmpdir.
"""


def test_product_data_repository_with_real_json_file(
        product_1: Product,
        product_2: Product,
        product_1_data: ProductDataDict,
        product_2_data: ProductDataDict,
        tmp_path: Path) -> None:
    filename = "test_products.json"
    test_file = tmp_path / filename

    sample_data = [product_1_data, product_2_data]

    with open(test_file, 'w') as file:
        json.dump(sample_data, file)

    product_json_file_reader = ProductJsonFileReader()
    validator = ProductDataDictValidator()
    converter = ProductConverter()

    product_data_repository = ProductDataRepository(
        file_reader=product_json_file_reader,
        validator=validator,
        converter=converter,
        filename=str(test_file)
    )
    data = product_data_repository.get_data()

    assert len(data) == 2
    assert data[0] == product_1
    assert data[1] == product_2
