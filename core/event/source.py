#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Campermote server
#
# Copyright (c) 2014 Leevi Põldaru, Mattias Põldaru
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc., 59
# Temple Place, Suite 330, Boston, MA 02111-1307 USA

from core.variable import types

class Source:
  parent = None
  name = ''
  display_name = ''
  description = ''
  # List of variables which are provided by the source.
  variables = []

  def __init__(self, parent):
    self.parent = parent

  def fire(self, data):
    self.parent.fire(data)