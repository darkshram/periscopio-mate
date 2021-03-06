# -*- coding: utf-8 -*-

#   This file is part of periscopio.
#   Copyright (c) 2008-2011 Patrick Dessalle <patrick@dessalle.be>
#   Copyright (c) 2017 Joel Barrios <darkshram@gmail.com>
#
#    periscopio is free software; you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    periscopio is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with periscopio; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from setuptools import setup
import shutil
import os
import version

PACKAGE = 'periscopio-mate'
VERSION = version.VERSION

try:
	os.makedirs("./debian/periscopio-mate/usr/share/caja-python/extensions")
except:
	pass
shutil.copy('periscopio-caja/periscopio-caja.py', 'debian/periscopio-mate/usr/share/caja-python/extensions')
