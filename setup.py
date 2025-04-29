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
    # Optional metadata
    author="Kelompok B1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Set minimum Python version
)
