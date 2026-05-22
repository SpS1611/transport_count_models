from setuptools import setup, find_packages

setup(
    name="tcm",
    version="0.1.0",
    description="Transport count data modeling with R-backed regression models",
    author="SHIVAM SHUKLA",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "rpy2",
    ],
    python_requires=">=3.10",
)