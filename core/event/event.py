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

from core.event.source import Source
from core.event.condition import Condition
from core.event.action import Action


class Events:
  events = []
  looping_events = []

  def __init__(self):
    pass

  def loop(self):
    for event in self.events:
      if event.looping:
        event.called()


class Event:
  name = ''
  display_name = ''
  description = ''
  looping = False
  sources = []
  conditions = []
  actions = []

  def __init__(self):
    pass

  def called(self, data):
    for condition in self.conditions:
      if condition.test(data):
        self.fire(condition, data)

  def fire(self, condition, data):
    for action in condition.actions:
      action.fire(condition, data)

# Example event
#onload = Event()
#onload.name = 'onload'
#onload.display_name = 'On loading'
#onload.description = 'Event is fired when device loads something'
#onload.add_condition()
#onload.add_action()
#onload