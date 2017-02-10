#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --

import importlib, os, re, sys, time


debug_mode = False
output_type= 'plain text'

def debug(**kwrgs):
    code = sys._getframe(1).f_code
    info = '{} {}:{}:{}'.format(
        time.strftime('%Y-%m-%d %H:%M:%S'),
        os.path.basename(code.co_filename),
        code.co_name,
        code.co_firstlineno)

    for key in kwrgs:
        print('{} {} : {}'.format(info, key, kwrgs[key]))

def execute_command(cmd, lower=False):
    result = []
    if re.search('2>&1', cmd) == None:
        cmd += ' 2>&1 '

    if re.search('cat', cmd) == None:
        cmd += ' | cat '

    with os.popen(cmd) as fd:
        result = fd.readlines()

    result = trim_list(result, lower)
    if debug_mode:
        print('[[[[[cmd]]]]]\n', '\n'.join(cmd) if isinstance(cmd, list) else cmd)
        if len(result):
            print('[[[[[result]]]]]\n', '\n'.join(result) if isinstance(result, list) else result)
        else:
            print('\n')

    return result

def trim_list(raw, lower=False):
    if raw == None:
        return []

    if len(raw) == 0:
        return []

    result = []
    if isinstance(raw, str):
        raw = raw.split('\n')

    for line in raw:
        line = line.strip()
        if lower:
            line = line.lower()
        if len(line) == 0:
            continue
        result.append(line)

    return result



def import_dir(path):
    '''
    디렉토리 내 python 모듈 import

    :param path: 경로
    :return: import 성공한 모듈 리스트
    '''
    result = []

    path = re.sub('^./','',path)

    for file in os.listdir(path):
        if '.py' != os.path.splitext(file)[1]:
            continue

        if file in ['__init__.py']:
            continue

        if file.startswith('test_'):
            continue

        module_name = '{}.{}'.format(re.sub('[\/]','.',path),os.path.splitext(file)[0])
        try:
            importlib.import_module(module_name)
            result.append(module_name)
        except ImportError as e:
            print('got error {!r}, errno is {}'.format(e, e.args[0]))

    return result



