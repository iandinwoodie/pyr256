# setup.py for pyR256

from distutils.core import setup

setup(
    name = "pyR256",
    packages = ["pyR256"],
    version = "0.0.2",
    description = "R256 command package",
    author = "Ian Dinwoodie",
    author_email = "dinwoodieian@gmail.com",
    url = "http://www.ianrobert.com",
    keywords = ["R256", "RMS", "Lin Engineering", "Motion", "Controller"],
    classifiers = [
		"Programming Language :: Python",
		"Development Status :: 2 - Pre-Alpha",
		"Environment :: Other Environment",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
		"Operating System :: OS Independent",
		"Topic :: Software Development :: Libraries :: Python Modules",
	],
	install_requires = [
		"pySerial",
	],
)