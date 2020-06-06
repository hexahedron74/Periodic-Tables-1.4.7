from setuptools import setup, find_packages
import PeriodicTables
setup(
    name='PeriodicTables',
    version='1.4.7',
    packages=find_packages(exclude=['docs', 'example']),
    url='',
    author = 'JWare Soft Development Team',
    author_email = 'ithan0704@naver.com',
    python_requires  = '>=3',
    zip_safe=False,
    description='The new Version of Periodic Tables'
)
