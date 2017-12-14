#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='overwatch-pagerduty',
    version='0.0.1',
    author='Petr Messner',
    author_email='petr.messner@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['doc', 'tests']),
    install_requires=[
        'requests',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'overwatch-pagerduty=overwatch_pagerduty:overwatch_pagerduty_main',
        ],
    },
)
