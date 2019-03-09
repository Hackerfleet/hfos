#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(
    name="hfos",
    version="1.2.1",
    description="hfos - an operating system for vessels",
    author="Hackerfleet Community",
    author_email="riot@c-base.org",
    url="https://github.com/Hackerfleet/hfos",
    license="GNU Affero General Public License v3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Isomer :: 1',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages(),
    include_package_data=True,
    long_description="""HFOS
====

A module to bundle Hackerfleet's Isomer modules to a ship computer operating system.

This software package is a plugin module for Isomer
""",
    dependency_links=[],
    install_requires=[
        'isomer',
        'hfos-alert',
        'hfos-anchor',
        'hfos-busrepeater',
        'hfos-comms',
        'hfos-crew',
        'hfos-dashboard',
        'hfos-dev',
        'hfos-equipment',
        'hfos-logbook',
        'hfos-map',
        # 'hfos-mesh',
        'hfos-navdata',
        'hfos-nmea',
        'hfos-nodestate',
        'hfos-webguides'
    ],
    entry_points="""[isomer.components]
    hfoscore=isomer.hfos.core:HFOSCore
    [isomer.schemata]
    """,
    test_suite="tests.main.main",
)
