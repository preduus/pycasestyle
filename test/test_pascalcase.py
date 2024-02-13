import unittest

from pycasestyle.pascalcase import PascalCase


class TestPascalCase(unittest.TestCase):
    def setUp(self):
        self.pascal_case_instance = PascalCase()

    def test_from_string(self):
        self.assertEqual(self.pascal_case_instance.from_string("I want a camel"), "IWantACamel")

    def test_from_string_with_empty_string(self):
        self.assertEqual(self.pascal_case_instance.from_string(""), "")

    def test_from_string_with_special_characters(self):
        self.assertEqual(self.pascal_case_instance.from_string("!$%"), "")

    def test_from_string_with_numbers(self):
        self.assertEqual(self.pascal_case_instance.from_string("123abc"), "123abc")

    def test_from_dict(self):
        input_dict = {"I want a camel": True}
        expected_output = {"IWantACamel": True}
        self.assertEqual(self.pascal_case_instance.from_dict(input_dict), expected_output)

    def test_from_dict_with_empty_dict(self):
        self.assertEqual(self.pascal_case_instance.from_dict({}), {})

    def test_from_dict_with_multiple_entries(self):
        input_dict = {"I want a camel": True, "Another key": False}
        expected_output = {"IWantACamel": True, "AnotherKey": False}
        self.assertEqual(self.pascal_case_instance.from_dict(input_dict), expected_output)


if __name__ == '__main__':
    unittest.main()
