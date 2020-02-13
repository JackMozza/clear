import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clear-moz", 
    version="0.0.1",
    author="Moz",
    author_email="skewer05@icloud.com",
    description="Clear function for my stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JackMozza/clear",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
