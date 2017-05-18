from distutils.core import setup

setup(
    name='tci-postman',
    version='0.1',
    author='Vincent Agnano',
    license='Copyright Anthropedia',
    long_description=open('readme.md').read(),
    install_requires=[
        'Flask-Mail<0.9.999',
    ],
)
