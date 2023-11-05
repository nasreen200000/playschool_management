from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in playschool_management/__init__.py
from playschool_management import __version__ as version

setup(
	name="playschool_management",
	version=version,
	description="playschool management system",
	author="nasreen",
	author_email="nasreen@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
