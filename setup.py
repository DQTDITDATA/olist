from setuptools import find_packages, setup

setup(
    name="olist_etl",
    packages=find_packages(exclude=["ETL_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)