from setuptools import setup, find_packages

setup(
    name="dummy-pkg",
    version="0.1.0",
    packages=find_packages(),
    author="Test User",
    author_email="test@example.com",
    description="A dummy package for testing RepoForge publish action.",
    python_requires=">=3.6",
)
