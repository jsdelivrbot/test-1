import unittest
from operation import add, substract

class OperationTest(unittest.TestCase):
    def add_test(self):
        self.assertEqual(add(1, 2), 3)

    # def substract_test(self):
    #     self.assertEqual(substract(4, 1), 3)
