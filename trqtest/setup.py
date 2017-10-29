
from setuptools import setup

setup (
    name='trqtest', 
    version='1.0',
    py_modules=['trqtest'],
    install_requires=[
        'rq',
    ],
    entry_points = {
        'console_scripts': ['trqtest=trqtest:mainsub'],
    }
)

