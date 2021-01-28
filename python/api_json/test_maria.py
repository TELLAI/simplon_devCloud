from code_maria import read_json
from code_maria import read_links

import unittest
import os.path


class TestStringMethods(unittest.TestCase):

    def test_json(self):
        read_json()
        self.assertTrue(os.path.isfile('stop_areas_maria.json'))
    def test_dict(self):
        read_links()
        self.assertEqual(type(links), list)

if __name__ == '__main__':
    unittest.main()