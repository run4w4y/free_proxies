import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="free_proxies",
    version="0.1.0",
    author="Vadim Makarov",
    author_email="add4che@gmail.com",
    description="Free proxies for the use with run4w4y/async_web_scrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/run4w4y/free_proxies",
    packages=setuptools.find_packages(),
    install_requires=[
        'trio'
    ],
    dependency_links=[
        'http://github.com/run4w4y/async_web_scrapper/tarball/main'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)