#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --

import re, inspect

class obj_plugin(object):
    def __init__(self):
        pass

    def get_method_list(self):
        '''
        class에  구현된 함수 리스트 리턴
        이름 앞 뒤 '__' 가 포함된 항목 제외
        :return: 함수 리스트
        '''
        return [name for name in dir(self)
                if name not in dir(self.__dir__)
                and re.search(r'\b__.*__\b', name) == None
                and inspect.ismethod(getattr(self,name))]

    def get_variable_list(self):
        '''
        class에  선언된 변수 리스트 리턴
        이름 앞 뒤 '__' 가 포함된 항목 제외
        :return: 변수 리스트
        '''
        return [name for name in dir(self)
                if name not in dir(self.__dir__)
                and re.search(r'\b__.*__\b', name) == None
                and False == inspect.ismethod(getattr(self,name))]

    def get_help(self):
        result = []
        return result
