from pycasestyle.abstract.case import Case
from pycasestyle.libs.string import clear_string, replacement


class KebabCase(Case):
    def from_string(self, value: str) -> str:
        """
        Returns the text converted to kebabcase style

            Parameters:
                    value (string): The text you need convert to kebabcase

            Returns:
                    kebabcase text (str): Text in kebabcase style

            Example:
                    print(kebabcase.from_string("I want a kebab") # => "i-want-a-kebab"
        """
        value = clear_string(value)
        value = value.lower()
        if value.strip() == "":
            return ""
        return replacement(r'\s+', value, '-')

    def from_dict(self, __dict: dict) -> dict:
        """
        Returns the dict converted all keys to kebabcase style

            Parameters:
                    __dict (dict): The text you need convert to kebabcase

            Returns:
                    kebabcase dict (dict): Dict with keys in kebabcase style

            Example:
                    print(kebabcase.from_dict({"I want a kebab": True}) # => {"i-want-a-kebab": True}
        """
        kebab_case_dict = {}
        for key, value in __dict.items():
            kebab_case_key = self.from_string(key)
            if isinstance(value, dict):
                value = self.from_dict(value)
            kebab_case_dict[kebab_case_key] = value
        return kebab_case_dict
