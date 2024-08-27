#!/usr/bin/env python3
"""
Test client
"""


import unittest
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class

from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)

class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The organization name to pass to
            GithubOrgClient.
            mock_get_json (Mock): The patched version of get_json.
        """

        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self) -> None:
        """
        Tests the _public_repos_url property.
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock,
                  ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
