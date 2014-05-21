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

class HardwareModule:
  device = None
  sources = []
  actions = []
  responses = []

  def __init__(self, device):
    self.device = device

  def event_ping(self, data):
    pass

  def action_ping(self):
    self.device.send('ping', 'cardreader')
