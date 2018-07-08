import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxyscraper",
    version="0.0.1",
    author="Ovidijus Okinskas",
    author_email="ovidijus.okinskas@gmail.com",
    description="Scrape proxy details from popular web pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okinskas/proxyscraper",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
