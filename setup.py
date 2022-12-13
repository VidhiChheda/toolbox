# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:07:57 2022

@author: admin
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3',
    author='Vidhi Chheda',
    author_email='vidhi@swancapital.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vidhi-chheda/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/vidhi-chheda/toolbox/issues"
    },
    #license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)