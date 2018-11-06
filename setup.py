#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
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

setup(name="hfos-projector",
      version="0.0.1",
      description="hfos-projector - a module for projecting visual maps",
      author="Hackerfleet Community",
      author_email="riot@c-base.org",
      url="https://github.com/hackerfleet/hfos-projector",
      license="GNU Affero General Public License v3",
      packages=find_packages(),
      long_description="""HFOS - Projector
================

A module to project visual maps.

This software package is a plugin module for HFOS.
""",
      dependency_links=[],
      install_requires=[
          'hfos>=1.2.0'
      ],
      entry_points="""[isomer.components]
    projectorr=hfos.projector.projector:Projector
    [isomer.schemata]
    scene=hfos.projector.scene:Scene
    """,
      test_suite="tests.main.main",
      )
