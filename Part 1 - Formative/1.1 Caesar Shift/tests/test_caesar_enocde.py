from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import caesar_encode

class TestCaesarEncode(TestCase):
    def test_encode(self):
        self.assertEqual(caesar_encode("HELLOWORLD",  5) , "MJQQTBTWQI" )


