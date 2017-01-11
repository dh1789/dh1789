#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --
"""
dh1789 : Utility methods and classes for providers

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
from pelix.ipopo.decorators import Provides, Property

import dh1789

import time,inspect

# ------------------------------------------------------------------------------

# Documentation strings format
__docformat__ = "restructuredtext en"

# Version
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# ------------------------------------------------------------------------------

def debug(**kwrgs):
    callerframerecord = inspect.stack()[1]  # 0 represents this line
    # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)

    info = '{} {}:{}:{}'.format(
        time.strftime('%Y-%m-%d %H:%M:%S'),
        info.filename,
        info.function,
        info.lineno,
    )

    for key in kwrgs:
        print('{} {} : {}'.format(info, key, kwrgs[key]))


@Provides(dh1789.SERVICE_PROVIDER_CONDITION)
@Property('_id', dh1789.SERVICE_PROVIDER_ID_CONDITION)
@Property('_title', dh1789.SERVICE_PROVIDER_TITLE_CONDITION)
class base_condition(object):
    """
    Mother class for condition providers
    """
    def __init__(self):
        """
        Sets up members
        """
        # Properties
        self._id = None
        self._title = None

    def get_id(self):
        """
        Returns the ID of the condition
        """
        return self._id

    def get_title(self):
        """
        Returns the title of the condition
        """
        return self._title


@Provides(dh1789.SERVICE_PROVIDER_TEST)
@Property('_id', dh1789.SERVICE_PROVIDER_ID_TEST)
@Property('_title', dh1789.SERVICE_PROVIDER_TITLE_TEST)
class base_test(object):
    """
    Mother class for test providers
    """
    def __init__(self):
        """
        Sets up members
        """
        # Properties
        self._id = None
        self._title = None

    def get_id(self):
        """
        Returns the ID of the condition
        """
        return self._id

    def get_title(self):
        """
        Returns the title of the condition
        """
        return self._title
