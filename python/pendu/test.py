from classPendu import Word
import unittest
import os.path


class TestStringMethods(unittest.TestCase):

    def test_list(self):
        my_word = Word()
        my_word.randWord()
        self.assertEqual(type(my_word.name), list)

    def test_len(self):
        my_word = Word()
        my_word_2 = Word()
        my_word.randWord()
        my_word_2.fct_create(my_word.name)
        self.assertEqual(len(my_word.name), len(my_word_2.name))

    def test_is(self):
        self.assertIsInstance(my_word)

if __name__ == '__main__':
    unittest.main()