from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in toolboxx/__init__.py
from toolboxx import __version__ as version

setup(
	name="toolboxx",
	version=version,
	description="A simple app with many usefull utils functions",
	author="Vinay Rawat",
	author_email="vineyrawat@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
