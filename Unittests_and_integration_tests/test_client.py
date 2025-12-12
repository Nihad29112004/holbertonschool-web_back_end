#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns expected value"""
        expected_payload = {"payload": True}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""

        mocked_payload = {"repos_url": "http://example.com/org/repos"}

        # Patch GithubOrgClient.org as a property
        with patch(
            "client.GithubOrgClient.org",
            new_callable=property,
            return_value=mocked_payload
        ):
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, "http://example.com/org/repos")
