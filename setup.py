import setuptools

setuptools.setup(
    name="literallyp1",
    version="0.1.0",
    url="TK",

    author="Rick Valenzuela",
    author_email="rv@rickv.com",

    description="A Twitter bot that scrapes, tweets headlines from certain newspaper front pages",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
