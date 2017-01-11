#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --
"""
Core module for the dh1789.

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

import dh1789

from dh1789.utils import debug

# ------------------------------------------------------------------------------

# Documentation strings format
__docformat__ = "restructuredtext en"

# Version
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# ------------------------------------------------------------------------------
import time,inspect, os
def debug(**kwrgs):
    callerframerecord = inspect.stack()[1]  # 0 represents this line
    # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)



    info = '{} {}:{}:{}'.format(
        time.strftime('%Y-%m-%d %H:%M:%S'),
        os.path.basename(info.filename),
        info.function,
        info.lineno,
        )

    for key in kwrgs:
        print('{} {} : {}'.format(info, key, kwrgs[key]))

@ComponentFactory('dh1789-core-factory')
@RequiresMap('_condition', dh1789.SERVICE_PROVIDER_CONDITION,
             dh1789.SERVICE_PROVIDER_ID_CONDITION, optional=True)
@RequiresMap('_test', dh1789.SERVICE_PROVIDER_TEST,
             dh1789.SERVICE_PROVIDER_ID_TEST, optional=True)
#@RequiresMap('_behavior', dh1789.SERVICE_BEHAVIOR_PROVIDER,
#             dh1789.SERVICE_BEHAVIOR_PROVIDER_ID, optional=True)
#@RequiresMap('_environment', dh1789.SERVICE_ENVIRONMENT_PROVIDER,
#             dh1789.SERVICE_ENVIRONMENT_PROVIDER_ID, optional=True)
@Instantiate('dh1789.core')
class dh1789_core(object):
    """
    dh1789
    """
    def __init__(self):
        """
        Sets up members
        """
        self._context = None

        self._condition = None
        self._behavior = None
        self._environment = None
        self._test = None

    @Validate
    def validate(self,context):
        """
        Component validated
        """
        self._context = context

        self.execute()

    def execute(self):
        self._test['ping'].set(ip='10.10.10.10')
        debug(result=self._test['ping'].execute())


