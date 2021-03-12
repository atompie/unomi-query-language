pip install wheel
python setup.py bdist_wheel
pip install twine
python -m twine upload dist/*


# if error pip install keyring==21.4.0