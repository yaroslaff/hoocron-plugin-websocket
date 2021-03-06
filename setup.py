#!/usr/bin/env python3

from setuptools import setup
import os
import sys



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='hoocron-plugin-websocket',
    version='0.0.1',
    packages=['hoocron_plugin.websocket'],

    install_requires=[
        'hoocron', 
        'python-socketio[client]',
        'websocket-client'],

    url='https://github.com/yaroslaff/hoocron-plugin-websocket',
    license='MIT',
    author='Yaroslav Polyakov',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author_email='yaroslaff@gmail.com',
    description='Websocket plugin for Hoocron',

    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
    ],
)
