from setuptools import setup, find_packages

setup(
    name="match-counter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pypdf"],
    entry_points={
        "console_scripts": [
            "match-counter=src.__main__:main",
        ],
    },
    python_requires=">=3.6",
    author="Your Name",
    description="A Python utility to count occurrences of a regular expression pattern in an RTF file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/match-counter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
