from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    description="A simple telegram bot",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="."),
    include_package_data=True,
    install_requires=[
        "adaptix>=3.0.0a5",
        "pytelegrambotapi>=4.13.0",
        "redis>=5.0.0",
        "toml>=0.10.2",
        "alembic>=1.13.1"
    ],
)
