import unittest
import main

class Test(unittest.TestCase):
    def test_find_most_common_word(self):
        self.assertEqual(main.find_most_common_word(), 'Самое часто повторяющееся слово: \"и\"')


if __name__ == '__main__':
    unittest.main()