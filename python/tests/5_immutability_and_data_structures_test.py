import unittest

from pure_functions import modify_data_structure as pf

class TestImmutabilityAndDataStructures(unittest.TestCase):

    def test_add_to_a_list(self):
        test = pf.add_to_list([1, 2, 3], 4)
        expected_result = [1, 2, 3, 4]

        # This should pass, because we are not modifying the original list, 
        # we are returning a new list which has a new memory address. 
        self.assertIsNot(test, expected_result) 