from distutils.core import setup
from setuptools import find_packages

setup(
    name='aapi',
    version='0.1.0',
    author='Aaron McSorley',
    author_email='a@aaronmcsorley.com',
    scripts=['bin/aapi'],
    url='https://github.com/amcsorley/aapi',
    license='Apache License, Version 2.0',
    description='A API',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['tornado', 'argparse',],
    data_files = [ ('/etc/init.d',['aapi/init-script/aapi']),
                   ('/etc/aapi',['aapi/config/aapi.conf']),
                   ('/usr/bin',['bin/aapi']),
                   ('/etc/pki/aapi',['aapi/certs/key.pem']),
                   ('/etc/pki/aapi',['aapi/certs/cert.pem']),
                   ('/etc/pki/aapi',['aapi/certs/openssl.cnf']),
    ],
)
