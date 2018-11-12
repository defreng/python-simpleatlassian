import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplejira",
    version="0.0.2",
    author="Alexander Hungenberg",
    author_email="alexander.hungenberg@gmail.com",
    description="A really basic JIRA REST Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/defreng/python-simplejira",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
