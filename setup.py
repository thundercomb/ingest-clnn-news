from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ingest-ncei-wind',
    version='0.1.0',
    description='Package for Climate News - Ingest NCEI Wind',
    long_description=readme,
    author='thundercomb',
    author_email='clappedthunder@gmail.com',
    url='https://github.com/thundercomb/ingest-ncei-wind',
    license=license,
    packages=find_packages(exclude=('test'))
)
