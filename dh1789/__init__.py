#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
dh1789 root package

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

# Module version
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Documentation strings format
__docformat__ = "restructuredtext en"

# ------------------------------------------------------------------------------

SERVICE_DH1789_PROVIDER = "dh1789"
"""
dh1789 provider service:
"""

SERVICE_PROVIDER_CONDITION = 'dh1789.condition'
SERVICE_PROVIDER_ID_CONDITION = 'dh1789.condition.id'
SERVICE_PROVIDER_TITLE_CONDITION = 'dh1789.condition.title'
#SERVICE_BEHAVIOR_PROVIDER = 'dh1789.behavior'
#SERVICE_BEHAVIOR_PROVIDER_ID = 'dh1789.behavior.id'
#SERVICE_ENVIRONMENT_PROVIDER = 'dh1789.environment'
#SERVICE_ENVIRONMENT_PROVIDER_ID = 'dh1789.environment.id'

SERVICE_PROVIDER_TEST = 'dh1789.test'
SERVICE_PROVIDER_ID_TEST = 'dh1789.test.id'
SERVICE_PROVIDER_TITLE_TEST = 'dh1789.test.title'

