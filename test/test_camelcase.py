import unittest
from pycasestyle.camelcase import CamelCase


class TestCamelCase(unittest.TestCase):
    def setUp(self):
        self.camel_case_converter = CamelCase()

    def test_from_string(self):
        self.assertEqual(self.camel_case_converter.from_string("I want a camel"), "iWantACamel")

    def test_from_dict(self):
        input_dict = {"I want a camel": True, "Another String": False}
        expected_output = {"iWantACamel": True, "anotherString": False}
        self.assertEqual(self.camel_case_converter.from_dict(input_dict), expected_output)


if __name__ == '__main__':
    unittest.main()