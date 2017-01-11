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



@ComponentFactory('dh1789-condition-factory')
@Property('_설명','condition.설명')
@Property('_이름','condition.이름')
@Provides('dh1789.condition')
class _condition(object):
    """
    test for the dh1789
    """
    def __init__(self):
        """
        Sets up members
        """
        self._context = None

        self._설명 = []
        self._이름 = ''
        self._항목 = []
        self._설정방법 = []
        self._확인방법 = []

    @Validate
    def validate(self, context):
        """
        Component validated

        :param context: Bundle Context
        """
        self._context = context

    def 항목_추가(self, 항목명, 설정방법, 확인방법):
        pass

    def 항목_삭제(self, 항목명):
        pass
