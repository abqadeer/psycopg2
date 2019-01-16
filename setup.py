import os
import re
from setuptools import find_packages, setup


READMEFILE = "README.md"
VERSIONFILE = os.path.join("psycopg2", "_version.py")
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"


def get_version():
    verstrline = open(VERSIONFILE, "rt").read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
            "Unable to find version string in %s." % VERSIONFILE)


setup(
    name='psycopg2',
    version=get_version(),
    description='psycopg2 package with static dependencies, for postgresql client library',
    long_description=open(READMEFILE).read(),
    url='https://github.com/abqadeer/psycopg2',
    author='',
    license='MIT',
    packages=find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
)
