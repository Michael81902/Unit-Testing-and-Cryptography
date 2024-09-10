import unittest
import sys
import os

from main import caesar_encode

class TestCaesar_Encode(TestCase):
    def test_encode(self):
        self.assertEqual(caesar_encode("Hello World"  4) "Lipps Asvph")

