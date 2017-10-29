
from setuptools import setup

setup (
    name='coggen', 
    version='1.0',
    py_modules=['coggen'],
    install_requires=[
        'rq',
    ],
    entry_points = {
        'console_scripts': ['coggen=coggen:mainsub'],
    }
)

