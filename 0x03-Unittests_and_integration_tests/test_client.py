#!/usr/bin/env python3
"""
Test client
"""


import unittest
from typing import Dict
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
        Testing the _public_repos_url property.
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Testing the public_repos method.
        """

        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 1697149,
                    "name": "cool-app",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342084,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/cool-app",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 17,
                    "default_branch": "main",
                },
                {
                    "id": 8560972,
                    "name": "keratus",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1332094,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/keratus",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 30,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "cool-app",
                    "keratus",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Testing the has_license method.
        """
        test_client = GithubOrgClient("google")
        confirm_license = test_client.has_license(repo, key)
        self.assertEqual(confirm_license, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Performs integration tests for the `GithubOrgClient` class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Prepare class
        """

        route_pl = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(this_url):
            if this_url in route_pl:
                return Mock(**{'json.return_value': route_pl[this_url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        Testing public_repos method.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """
        Testing license for public_repos method
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Unsets the class fixtures after tests.
        """
        cls.get_patcher.stop()
