from setuptools import setup, find_packages

setup(
    name='InstaBot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'instabot',
        'schedule',
    ],
)
