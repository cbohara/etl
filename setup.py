from setuptools import setup, find_packages

with open('/Users/charlieohara/Documents/Egnyte/Private/charlie.ohara/code/github/cbohara/etl/requirements.txt') as fd:
    requirements = [line.rstrip() for line in fd]

setup(
    name='etl',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
)
