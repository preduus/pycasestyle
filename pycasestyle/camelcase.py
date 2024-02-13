from pycasestyle.abstract.case import Case
from pycasestyle.libs.string import clear_string


class CamelCase(Case):
    def from_string(self, value: str) -> str:
        """
        Returns the text converted to camelcase style

            Parameters:
                    value (string): The text you need convert to camelcase

            Returns:
                    camelcase text (str): Text in camelcase style

            Example:
                    print(camelcase.from_string("I want a camel") # => "iWantACamel"
        """
        value = clear_string(value)
        if value.strip() == "":
            return ""
        words = value.split()
        camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
        return ''.join(camel_case_words)

    def from_dict(self, __dict: dict) -> dict:
        """
        Returns the dict converted all keys to camelcase style

            Parameters:
                    __dict (dict): The text you need convert to camelcase

            Returns:
                    camelcase dict (dict): Dict with keys in camelcase style

            Example:
                    print(camelcase.from_dict({"I want a camel": True}) # => {"iWantACamel": True}
        """
        camel_case_dict = {}
        for key, value in __dict.items():
            camel_case_key = self.from_string(key)
            if isinstance(value, dict):
                value = self.from_dict(value)
            camel_case_dict[camel_case_key] = value
        return camel_case_dict
