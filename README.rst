pycasestyle
===========

pycasestyle is a Python library for converting variable naming styles between CamelCase, snake_case, kebab-case, and PascalCase.

Supported styles:
    - CamelCase
    - SnakeCase
    - KebabCase
    - PascalCase

Installation
------------

To install pycasestyle, you can use pip:

.. code-block:: bash
    pip install pycasestyle

Usage
-----

You can import the text formatting styles directly from the pycasestyle module and use them in your code. Here's an example of how to use the text formatting styles:

.. code-block:: python
    import pycasestyle

    # Converting to camelcase from text
    camelcased_text = pycasestyle.camelcase.from_string("i want a camel")
    print(camelcased_text)  # Output: "iWantACamel"

    # Converting to camelcase from dict
    camelcased_dict = pycasestyle.camelcase.from_dict({"i want a camel": "value"})
    print(camelcased_dict)  # Output: {"iWantACamel": "value"}

    # Converting to snakecase from text
    snakecased_text = pycasestyle.snakecase.from_string("I Want A Snake")
    print(snakecased_text)  # Output: "i_want_a_snake"

    # Converting to snakecase from dict
    snakecased_dict = pycasestyle.snakecase.from_dict({"I Want A Snake": "value"})
    print(snakecased_dict)  # Output: {"i_want_a_snake": "value"}

    # Converting to kebab-case
    kebabcased_text = pycasestyle.kebabcase.from_string("I Want A Kebab")
    print(kebabcased_text)  # Output: "i-want-a-kebab"

    # Converting to kebab-case from dict
    kebabcased_dict = pycasestyle.kebabcase.from_dict({"I Want A Kebab": "value"})
    print(kebabcased_dict)  # Output: {"i-want-a-kebab": "value"}

    # Converting to PascalCase from text
    pascalcased_text = pycasestyle.pascalcase.from_string("i want a pascal")
    print(pascalcased_text)  # Output: "IWantAPascal"

    # Converting to PascalCase from dict
    pascalcased_dict = pycasestyle.pascalcase.from_dict({"i want a pascal": "value"})
    print(pascalcased_dict)  # Output: {"IWantAPascal": "value"}
Use cases
------------
If you needed convert schemas, mappings, contracts, etc. This tool is specific to turn easily your job.

Real use case:

You need to migrate information from Postgres to Elasticsearch, however, the mapping used in Elastic is following the camelcase pattern, whereas in Postgres it is with the Snakecase pattern, see how simple it is to solve:


.. code-block:: python
    import pycasestyle

    postgres_contract = {
        "id": 1,
        "customers_id": 32,
        "users_id": 56,
        "period_datetime": "2024-08-10"
    }

    elastic_contract = pycasestyle.camelcase.from_dict(postgres_contract)
    print(elastic_contract) # Output: {
        "id": 1,
        "customersId": 32,
        "usersId": 56,
        "periodDatetime": "2024-08-10"
    }

Contributing
------------

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the `GitHub repository <https://github.com/preduus/pycasestyle>`.

License
-------

This project is licensed under the Apache License 2.0 License. See the `LICENSE <https://github.com/preduus/pycasestyle/LICENSE>` file for more details.