import unittest

from edge_cases import rearrange_name

class TestRearrange(unittest.TestCase):


    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
