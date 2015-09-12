from elapsed import __version__

from setuptools import setup, find_packages

setup(
    name='elapsed.py',
    version=__version__,
    license='MIT',
    url='https://github.com/fuzeman/elapsed.py',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    description='Simple expression/function profiler',
    packages=find_packages(exclude=[
        'examples'
    ]),
    platforms='any',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
)