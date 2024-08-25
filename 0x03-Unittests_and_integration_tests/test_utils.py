#!/usr/bin/env python3
"""
Unittests Module
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the utils.access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with different nested maps and paths.

        Parameters:
        - nested_map: The dictionary to retrieve the value from.
        - path: A tuple representing the sequence of keys to access the value.
        - expected: The expected result after accessing the nested map.

        The method checks if the value returned by access_nested_map
        matches the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map to ensure a KeyError is raised for invalid
        paths.

        Parameters:
        - nested_map: The dictionary to attempt to retrieve the value from.
        - path: A tuple representing the sequence of keys to access the value.

        The method checks if the access_nested_map function raises a KeyError
        when attempting to access a key that does not exist in the nested map.
        Also verifies that the exception message is as expected.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), str(path[-1]))


if __name__ == "__main__":
    unittest.main()

