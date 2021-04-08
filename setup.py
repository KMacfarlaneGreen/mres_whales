from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="Katie Green",
    author_email="author@example.com",
    description="Masters research project ai4er",
    url="url-to-github-page",
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
)
