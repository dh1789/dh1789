import unittest
import plugin.mysql


class test_mysql(unittest.TestCase):
    def test_get_method_list(self):
        a = plugin.mysql.plugin_mysql()
        print(a.get_method_list())
#        self.assertEqual(True, False)

    def test_get_variable_list(self):
        a = plugin.mysql.plugin_mysql()
        print(a.get_variable_list())

    def test_import_plugin(self):
        a = plugin.mysql.plugin_mysql()
        print(a.get_variable_list())






if __name__ == '__main__':
    unittest.main()
