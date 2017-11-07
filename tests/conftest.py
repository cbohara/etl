import pytest


@pytest.fixture(scope='session')
def comma_sep_csv(tmpdir_factory):
    csv = tmpdir_factory.mktemp('tmpdir').join('demo_csv.csv')
    csv.write('apple,banana,cashew')
    return csv
