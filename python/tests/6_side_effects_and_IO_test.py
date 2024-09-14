import unittest

from pure_functions import side_effects_and_IO as pf

class TestSideEffectsAndIO(unittest.TestCase):

    # How to isolate a side effect from a pure function
    def test_side_effect_handling(self):
        file_word_count = 5
        side_effect_output = pf.get_file()
        test = pf.count_words(side_effect_output)
        self.assertEqual(test, file_word_count)
