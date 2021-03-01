from setuptools import find_packages, setup

setup(name='mylib',
      packages=find_packages(include=['mylib']),
      version='0.1.11',
      description='My Codes Python library',
      author='Mina Mousavifar',
      license='MIT',
      install_requires=[],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      test_suite='tests',
      )
