import setuptools

from pom_elements import __version__ as vs

with open("README.md", "r") as fh:
    for _ in range(4):
        next(fh)
    long_description = fh.read()

setuptools.setup(
    name="pom-elements",
    version=vs,
    author="Nick Beaird",
    author_email="nicklasbeaird@gmail.com",
    description="The Python Page Object Model that extends to Page Elements",
    long_description=long_description,
    url="https://github.com/nickbeaird/pom-elements",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
