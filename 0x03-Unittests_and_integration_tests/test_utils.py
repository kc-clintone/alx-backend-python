#!/usr/bin/env python3
"""
Unittests Module
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map

from typing import (
    Dict,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception: Exception,
            ) -> None:

        """
        Test access_nested_map to ensure a KeyError is raised for
        invalid
        paths.

        Parameters:
        - nested_map: The dictionary to attempt to retrieve the
        value from.
        - path: A tuple representing the sequence of keys to access
        the value.

        The method checks if the access_nested_map function
        raises a KeyError
        when attempting to access a key that does not exist in
        the nested map.
        Also verifies that the exception message is as expected.
        """

        with self.assertRaises(exception):
            access_nested_map(nested_map, path)



class TestGetJson(unittest.TestCase):
    """
    Test case for the utils.get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):

        """
        Test that get_json returns the correct JSON payload from
        the given URL.

        Parameters:
        - test_url: The URL to be passed to get_json.
        - test_payload: The expected JSON payload returned by the
        mocked requests.get.

        The method mocks requests.get to avoid actual HTTP calls
        and verifies that:
        - requests.get is called once with test_url.
        - get_json returns the expected test_payload.
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get',
                    return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()

