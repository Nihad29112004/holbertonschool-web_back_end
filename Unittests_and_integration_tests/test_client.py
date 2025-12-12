#!/usr/bin/env python3
"""Github org client"""

import requests


def get_json(url):
    """Fetch JSON data"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Github Org Client"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        self._org_name = org_name

    @property
    def org(self):
        """Return organization information"""
        url = self.ORG_URL.format(org=self._org_name)
        return get_json(url)
