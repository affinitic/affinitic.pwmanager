from setuptools import setup, find_packages
import os

version = '0.6.dev0'

setup(name='affinitic.pwmanager',
      version=version,
      description="Password manager utility",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Affinitic',
      author_email='jfroche@affinitic.be',
      url='http://svn.affinitic.be/python',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['affinitic'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.interface'
      ])
