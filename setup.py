from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Jateendra",
    description="dvc-ml pipeline designing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jateendra/DVC-MachineLearning-AIOPs",
    author_email="jateendra.pradhan@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)