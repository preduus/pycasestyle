import unittest

from pycasestyle.kebabcase import KebabCase


class TestKebabCase(unittest.TestCase):
    def setUp(self):
        self.kebab_case_instance = KebabCase()

    def test_from_string(self):
        self.assertEqual(self.kebab_case_instance.from_string("I want a camel"), "i-want-a-camel")

    def test_from_string_with_empty_string(self):
        self.assertEqual(self.kebab_case_instance.from_string(""), "")

    def test_from_string_with_special_characters(self):
        self.assertEqual(self.kebab_case_instance.from_string("!$%"), "")

    def test_from_string_with_numbers(self):
        self.assertEqual(self.kebab_case_instance.from_string("123abc"), "123abc")

    def test_from_dict(self):
        input_dict = {"I want a camel": True}
        expected_output = {"i-want-a-camel": True}
        self.assertEqual(self.kebab_case_instance.from_dict(input_dict), expected_output)

    def test_from_dict_with_empty_dict(self):
        self.assertEqual(self.kebab_case_instance.from_dict({}), {})

    def test_from_dict_with_multiple_entries(self):
        input_dict = {"I want a camel": True, "Another key": False}
        expected_output = {"i-want-a-camel": True, "another-key": False}
        self.assertEqual(self.kebab_case_instance.from_dict(input_dict), expected_output)


if __name__ == '__main__':
    unittest.main()
