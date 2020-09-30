import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="st-rewrite",
    version="0.0.1",
    author="Anjith George",
    author_email="anjith2006@gmail.com",
    description="A forward backward rewriter.",
    license="BSD 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anjith2006/Rewrite",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=["htbuilder"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)