import pytest
from extract import single_file


def test_comma_sep_csv_content(comma_sep_csv):
    """Ensure the header is read from the input file"""
    csv = comma_sep_csv.read()
    assert csv == 'apple,banana,cashew'
