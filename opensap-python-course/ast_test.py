import ast
import unittest

from attr import Attribute

class Simpletest(unittest.TestCase):

    def test_true(self):
        
        is_true = False
        with open("opensap-python-course\week4u5.py", 'r') as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if (
                    isinstance(node, ast.Call)  # It's a call
                    and isinstance(node.func, ast.Name)  # It directly invokes a name
                    and node.func.id == "open"  # That name is `print`
                    ):
                # Check if any arg is the one we're looking for
                if any(
                    arg.value == "invoice_data.txt"
                    for arg in node.args
                    if isinstance(arg, ast.Constant)
                    ):
                    is_true = True
                print(is_true)
        
        self.assertTrue(is_true)


if __name__ == '__main__':
    unittest.main()