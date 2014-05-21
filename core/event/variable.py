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

class Variable:
  name = ''
  display_name = ''
  description = ''
  variable_class = None

  def __init__(self, variable_class, name, display_name, description):
    self.name = name
    self.display_name = display_name
    self.description = description
    self.variable_class = variable_class

  def __str__(self):
    return '<Variable "%s" type %s>' % (self.display_name, self.name)

types = {}
types['bool'] = Variable(bool, 'bool', 'Boolean',
    'Boolean can be either True or False.')
types['int'] = Variable(int, 'int', 'Integer',
    'Integer is an exact number.')
types['float'] = Variable(float, 'float', 'Float',
    'Floating point number may have decimal points.')
types['str'] = Variable(str, 'str', 'String',
    'String contains of characters. Unicode is preferred.')
types['list'] = Variable(list, 'list', 'List',
    'List is a simple vector of values.')
types['dict'] = Variable(dict, 'dict', 'Dictionary',
    'Dictionary is Python slang for associative array.')
