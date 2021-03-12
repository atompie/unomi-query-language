from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='unomi_query_language',
    version='0.1.2',
    description='Unomi Query Language library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['unomi_query_language'],
    install_requires=[
        'requests',
        'lark'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
