from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",  # updated version
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "pytest",
        "pytest-html",
    ],
    entry_points={
        "console_scripts": [
            "calc = main:main",  # Link your script with the function main()
        ],
    },
)
