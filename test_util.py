import unittest
from util import *


class test_import_dir(unittest.TestCase):
    def setUp(self):
        self._path='./test_tmp'

        execute_command('mkdir -p {}'.format(self._path))

    def tearDown(self):
        execute_command('rm -fr {}'.format(self._path))

    def make_dummy_python_file(self,name):
        execute_command('''echo "
class import_test(object):
    def __init__(self):
        pass
        " > {}/{}'''.format(self._path,name))

    def test_기본(self):
        self.make_dummy_python_file('aaa.py')
        self.assertEqual(['test_tmp.aaa'],import_dir(self._path))

    def test_init_예외처리(self):
        self.make_dummy_python_file('__init__.py')
        self.assertEqual([],import_dir(self._path))

    def test_test_예외처리(self):
        self.make_dummy_python_file('test_aaa.py')
        self.assertEqual([],import_dir(self._path))

if __name__ == '__main__':
    unittest.main()
