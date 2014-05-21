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

class CoreDevice:
  name = ''
  code = ''
  device = 'CoreDevice'
  modules = []
  sources = ['ping', 'online', 'battery', 'other']
  actions = ['ping', 'wakeup', 'sleep', 'reset', 'set_io', 'get_io']
  responses = ['ping']

  def __init__(self,  name, code):
    self.name = name
    self.code = code

  def setup(self, data):
    pass

  def send(self, command, data = None):
    pass

  def recieve(self, command, data):
    pass

  def list_all_events(self):
    events = []
    for event in self.events:
      events.append(event)
    for module in self.modules:
      for event in module.events:
        events.append(event)
    return events

  def event_ping(self):
    pass

  def event_online(self, data):
    self.setup(data)

  def event_battery(self, data):
    pass

  def event_other(self, data):
    pass

  def action_ping(self):
    pass

  def action_wakeup(self):
    pass

  def action_sleep(self):
    pass

  def action_set_io(self, pin, high=True):
    pass

  def action_get_io(self, pin):
    pass
