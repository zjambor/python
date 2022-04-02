import unittest
import connect_db as cdb
import cx_Oracle
import config as cfg

class Test_DBConnection(unittest.TestCase):
    def test_version(self):
        expected = '19'
        self.assertEqual(cdb.ver[0], expected)

    def test_conn(self):
        expected = 1
        self.assertEqual(cdb.check_conn_result, expected)

    def test_cursor(self):
        expected = 1
        self.assertGreaterEqual(cdb.cursor('select employee_id,last_name,job_id,manager_id,hire_date,salary,commission_pct,department_id from employees'), expected)

    def test_true(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()