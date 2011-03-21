import os
from setuptools import setup, find_packages, Extension
from platform import machine


fmodlib = "fmodex-4.32.09"
pdatalib = "libfmodex-4.32.09.so"
if machine() == "x86_64":
    fmodlib = "fmodex64-4.32.09"
    pdatalib = "libfmodex64-4.32.09.so"


pandora_module = Extension(
    'pypandora._pandora',
    sources = [
        'pypandora/_pandora/main.c',
        'pypandora/_pandora/crypt.c',
    ],
    include_dirs = ["pypandora/include"],
    library_dirs = ["pypandora/lib"],
    extra_link_args = ["-Wl,-rpath=./lib"],
    libraries = [fmodlib],
)

setup(
    name = "pypandora",
    version = "1.0",
    author = "Andrew Moffat",
    author_email = "andrew.moffat@medtelligent.com",
    url = "https://github.com/amoffat/pypandora",

    packages = find_packages('.'),
    package_dir = {'':'.'},
    data_files=[
        ('.', ['README']),
    ],
    package_data = {
        'pypandora': ['templates/*.xml'],
        'pypandora': ['lib/%s' % pdatalib],
    },
    include_package_data=True,

    keywords = "pandora api",
    description = "pandora client",
    install_requires=[
        'eventlet'
    ],
    classifiers = [
        "Intended Audience :: Developers",
        'Programming Language :: Python',
    ],
    ext_modules = [pandora_module]
)
