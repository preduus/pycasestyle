from pycasestyle.abstract.case import Case
from pycasestyle.libs.string import clear_string, split_string


class PascalCase(Case):
    def from_string(self, value: str) -> str:
        """
        Returns the text converted to pascalcase style

            Parameters:
                    value (string): The text you need convert to pascalcase

            Returns:
                    pascalcase text (str): Text in pascalcase style

            Example:
                    print(pascalcase.from_string("I want a pascal") # => "IWantAPascal"
        """
        value = clear_string(value)
        value = value.lower()
        if value.strip() == "":
            return ""
        parts = split_string(r'[_\s]+', value)
        return ''.join(part.capitalize() for part in parts)

    def from_dict(self, __dict: dict) -> dict:
        """
        Returns the dict converted all keys to pascalcase style

            Parameters:
                    __dict (dict): The text you need convert to pascalcase

            Returns:
                    pascalcase dict (dict): Dict with keys in pascalcase style

            Example:
                    print(pascalcase.from_dict({"I want a pascal": True}) # => {"IWantAPascal": True}
        """
        pascal_case_dict = {}
        for key, value in __dict.items():
            pascal_case_key = self.from_string(key)
            if isinstance(value, dict):
                value = self.from_dict(value)
            pascal_case_dict[pascal_case_key] = value
        return pascal_case_dict
