from code_maria import read_json
import unittest
import os.path


class TestStringMethods(unittest.TestCase):

    def test_json(self):
        read_json()
        self.assertTrue(os.path.isfile('stop_areas_maria.json'))

if __name__ == '__main__':
    unittest.main()