import unittest
# import connect_db as cdb
import cx_Oracle
# import config as cfg

class Test_DBConnection(unittest.TestCase):
    # def test_version(self):
    #     expected = '18'
    #     self.assertEqual(cdb.ver[0], expected)

    # def test_conn(self):
    #     expected = 1
    #     self.assertEqual(cdb.check_conn_result, expected)

    # def test_cursor(self):
    #     expected = 1
    #     self.assertGreaterEqual(cdb.cursor('select * from emp'), expected)

    def test_true(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()