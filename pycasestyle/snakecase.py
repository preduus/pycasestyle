from pycasestyle.abstract.case import Case
from pycasestyle.libs.string import clear_string, replacement


class SnakeCase(Case):
    def from_string(self, value: str) -> str:
        """
        Returns the text converted to snakecase style

            Parameters:
                    value (string): The text you need convert to snakecase

            Returns:
                    snakecase text (str): Text in snakecase style

            Example:
                    print(snakecase.from_string("I want a snake") # => "i_want_a_snake"
        """
        value = clear_string(value)
        value = value.lower()
        if value.strip() == "":
            return ""
        return replacement(r'\s+', value)

    def from_dict(self, __dict: dict) -> dict:
        """
        Returns the dict converted all keys to snakecase style

            Parameters:
                    __dict (dict): The text you need convert to snakecase

            Returns:
                    snakecase dict (dict): Dict with keys in snakecase style

            Example:
                    print(snakecase.from_dict({"I want a snake": True}) # => {"i_want_a_snake": True}
        """
        snake_case_dict = {}
        for key, value in __dict.items():
            snake_case_key = self.from_string(key)
            if isinstance(value, dict):
                value = self.from_dict(value)
            snake_case_dict[snake_case_key] = value
        return snake_case_dict
