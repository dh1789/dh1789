#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --
"""
dh1789 :  conditions

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
from pelix.ipopo.decorators import ComponentFactory, Requires, Validate, \
    Instantiate

from dh1789.utils import debug, base_condition


# ------------------------------------------------------------------------------

# Documentation strings format
__docformat__ = "restructuredtext en"

# Version
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# ------------------------------------------------------------------------------

@ComponentFactory('dh1789-conditions-factory')
@Instantiate('dh1789.conditions')
class conditions(base_condition):
    """
    condition for the dh1789
    """
    def __init__(self):
        """
        Sets up members
        """
        base_condition.__init__(self)

        self._context = None

    @Validate
    def validate(self, context):
        """
        Component validated

        :param context: Bundle Context
        """
        self._context = context

        self._id = 'conditions'
        self._title = 'Conditions'

