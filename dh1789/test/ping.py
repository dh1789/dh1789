#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --
"""
dh1789 :  test

:author: Lee Dong Ho
:copyright: Copyright 2016, Lee Dong Ho
:license: Apache License 2.0
:version: 0.0.1

..

    Copyright 2016 Lee Dong Ho

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

# iPOPO Decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, RequiresMap, Instantiate, Property, Validate

from dh1789.utils import debug, base_test
import dh1789

import subprocess


# ------------------------------------------------------------------------------

# Documentation strings format
__docformat__ = "restructuredtext en"

# Version
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# ------------------------------------------------------------------------------

PING_IP = 'ping.ip'
PING_SEND_COUNT = 'ping.send_count'
CONDITION_OF_SUCCESS_BY_PING_REPLY_COUNT = 'dh1789.test.ping.condition_of_success_by_ping_reply_count'


@ComponentFactory('dh1789-test-ping-factory')
@Property('_ip', PING_IP, '127.0.0.1' )
@Property('_send_count', PING_SEND_COUNT, 1)
@Instantiate('dh1789.test.ping')
class ping(base_test):
    """
    test for the dh1789
    """
    def __init__(self):
        """
        Sets up members
        """
        base_test.__init__(self)

        self._context = None

        self._ip = None
        self._send_count = None

    @Validate
    def validate(self, context):
        """
        Component validated

        :param context: Bundle Context
        """
        self._context = context

        self._id = 'ping'
        self._title = 'Ping'

    def execute(self):
        response = subprocess.call(['ping', '-c', str(self._send_count), '-W', '5', self._ip],stdout=open('/dev/null','w'),stderr=open('/dev/null','w'))
        return True if response == 0 else False

    def set(self,**kwargs):
        for key in kwargs:
            try:
                vars()['_'+key] = kwargs[key]
                print(key, kwargs[key])
                print(vars()['_'+key])
            except :
                print('error _'+key)
        print('ip=',self._ip,self._send_count)

