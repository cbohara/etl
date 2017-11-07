import pytest
from extract import single_file


@pytest.fixture(params=comma_sep_csv)
def test_comma_sep_csv_content():
    """Ensure the header is read from the input file"""
    print(csv)
