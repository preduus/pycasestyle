import unittest

from pycasestyle.snakecase import SnakeCase


class TestSnakeCase(unittest.TestCase):
    def setUp(self):
        self.snake_case_instance = SnakeCase()

    def test_from_string(self):
        self.assertEqual(self.snake_case_instance.from_string("I want a camel"), "i_want_a_camel")

    def test_from_string_with_empty_string(self):
        self.assertEqual(self.snake_case_instance.from_string(""), "")

    def test_from_string_with_special_characters(self):
        self.assertEqual(self.snake_case_instance.from_string("!$%"), "")

    def test_from_string_with_numbers(self):
        self.assertEqual(self.snake_case_instance.from_string("123abc"), "123abc")

    def test_from_dict(self):
        input_dict = {"I want a camel": True}
        expected_output = {"i_want_a_camel": True}
        self.assertEqual(self.snake_case_instance.from_dict(input_dict), expected_output)

    def test_from_dict_with_empty_dict(self):
        self.assertEqual(self.snake_case_instance.from_dict({}), {})

    def test_from_dict_with_multiple_entries(self):
        input_dict = {"I want a camel": True, "Another key": False}
        expected_output = {"i_want_a_camel": True, "another_key": False}
        self.assertEqual(self.snake_case_instance.from_dict(input_dict), expected_output)


if __name__ == '__main__':
    unittest.main()
