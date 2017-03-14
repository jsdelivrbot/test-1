import unittest
from operation import suma, resta

class OperationTest(unittest.TestCase):
    def suma_test(self):
        self.assertEqual(suma(1, 2), 3)

    # def resta_test(self):
    #     self.assertEqual(resta(4, 1), 3)
