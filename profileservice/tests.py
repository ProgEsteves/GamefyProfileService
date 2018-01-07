# -*- coding: utf-8 -*-
"""main"""

import unittest
import requests

class ProfileTestCase(unittest.TestCase):
    """Profile test case."""

    def test_welcome_200(self):
        """test welcome 200"""
        response = requests.post(url='http://localhost:8080/api/v0/welcome/ProgEsteves')
        self.assertEqual(requests.codes['ok'], response.status_code)

    def test_welcome_master(self):
        """test welcome master"""
        content = requests.post(url='http://localhost:8080/api/v0/welcome/ProgEsteves')
        self.assertEqual(b'Welcome Felipe Esteves', content.content)

if __name__ == '__main__':
    unittest.main()
