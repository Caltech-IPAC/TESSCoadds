import os

from setuptools import setup

setup(name='tess_coadds',
    version='1.0.0',
    author='John Good',
    author_email='jcg@ipac.caltech.edu',
    license='LICENSE.txt',
    keywords='astronomy, images',
    url = 'https://github.com/Caltech-IPAC/TESSCoadds',
    description='Cutouts from coadded TESS images',
    packages = ['tess_coadds'],
    install_requires = ['astropy', 'MontagePy'])
