import setuptools


with open("README.md") as file:
    long_desc = file.read()

with open("VERSION") as file:
    VERSION = file.read()


setuptools.setup(
    name="dashml",
    version=VERSION,
    author="Madelyn Eriksen",
    author_email="opensource@madelyneriksen.com",
    description="Generate HTML with Python functions.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/madelyneriksen/dashml",
    packages=["dashml"],
    install_requires=[
        "lxml",
        "markupsafe",
    ]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
