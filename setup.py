from setuptools import setup, find_packages
import os

version = '1.0'

requires = [
    'setuptools',
    'openprocurement.api>=2.4.4',
    'openprocurement.tender.core>=2.4.2',
]

test_requires = requires + [
    'webtest',
    'python-coveralls',
]

docs_requires = requires + [
    'sphinxcontrib-httpdomain',
]

entry_points = {
    'openprocurement.tender.core.plugins': [
        'frameworkagreement = openprocurement.tender.frameworkagreement.includeme:includeme',
    ],
}

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

setup(name='openprocurement.tender.frameworkagreement',
      version=version,
      description="",
      long_description=README,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='web services',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/openprocurement.tender.frameworkagreement',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.tender'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={'test': test_requires, 'docs': docs_requires},
      test_suite="openprocurement.tender.frameworkagreement.tests.main.suite",
      entry_points=entry_points,
      )
