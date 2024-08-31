#!/usr/bin/env python3
"""
Let's do some testing
"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import (GithubOrgClient)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Let's test the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, res: Dict, mock_function: MagicMock) -> None:
        """
        Then test the `org` method.
        """
        mock_function.return_value = MagicMock(return_value=resp)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), res)
        mock_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """
        Now testing the `_public_repos_url` property.
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_obj:
            mock_obj.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        We then test the `public_repos` method
        """
        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697249,
                    "name": "episodes.banger",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342014,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.banger",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 23,
                    "default_branch": "master",
                },
                {
                    "id": 8566772,
                    "name": "crap",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342014,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/crap",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 30,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as repos_url:
            repos_url.return_value = payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.banger",
                    "crap",
                ],
            )
            repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Testing the `has_license` method.
        """
        github_org_client = GithubOrgClient("google")
        client_license = github_org_client.has_license(repo, key)
        self.assertEqual(client_license, expected)


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
    This function integrates tests for the `GithubOrgClient` class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        And this sets up a class fixture before running tests.
        """
        payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in payload:
                return Mock(**{'json.return_value': payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        This function tests the `public_repos` method.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """
        And this tests the `public_repos` method using a license.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Unsets some functions after running all tests
        """
        cls.get_patcher.stop()
