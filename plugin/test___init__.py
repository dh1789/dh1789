import unittest
from plugin import *

class test_obj_plugin(unittest.TestCase):
    def setUp(self):
        self.a = obj_plugin()

    def test_obj_plugin_생성(self):
        self.assertTrue(self.a)

    def test_obj_plugin___get_method_list(self):
        self.assertIn('get_method_list',self.a.get_method_list())

    def test_obj_plugin___get_variable_list(self):
        self.assertEqual([],self.a.get_variable_list())

    def test_obj_plugin___get_help(self):
        self.assertEqual([],self.a.get_help())

if __name__ == '__main__':
    unittest.main()
