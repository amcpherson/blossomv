import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blossomv',
    version="v2.04",
    author="Andrew McPherson",
    author_email="andrew.mcpherson@gmail.com",
    description="A wrapper for the BlossomV code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amcpherson/blossomv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Research purposes only",
        "Operating System :: Linux",
    ],
)
