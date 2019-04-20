import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygeosolve",
    version="0.8.0",
    author="Sean Leavey",
    author_email="author@example.com",
    description="Geometric constraint solver for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SeanDS/pygeosolve",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3",
        "Operating System :: OS Independent",
    ],
)