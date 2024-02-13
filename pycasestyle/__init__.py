"""
pycasestyle.

A python case styles conversions lib.
Supported types:
    - CamelCase
    - SnakeCase
    - Kebab
    - Pascal
"""

__version__ = "1.0.0"
__author__ = 'Pedro Rodrigues'

from pycasestyle.camelcase import CamelCase as _CamelCase
from pycasestyle.snakecase import SnakeCase as _SnakeCase
from pycasestyle.kebabcase import KebabCase as _KebabCase
from pycasestyle.pascalcase import PascalCase as _PascalCase

camelcase = _CamelCase()
snakecase = _SnakeCase()
kebabcase = _KebabCase()
pascalcase = _PascalCase()

__all__ = ["camelcase", "snakecase", "kebabcase", "pascalcase"]