from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import caesar_encode

class TestCaesarEncode(TestCase):
    def test_encode(self):
        self.assertEqual(caesar_encode("HELLOWORLD",  5) , "MJQQTBTWQI" )
    def test_encode2(self):
        self.assertEqual(caesar_encode("HELLO WORLD", 5), "MJQQT BTWQI")
    def test_encode3(self):
        self.assertEqual(caesar_encode("HELLO WORLD!", 5), "MJQQT BTWQI!")
    def test_encode4(self):
        self.assertEqual(caesar_encode("hElLO WORLD!", 5), "MJQQT BTWQI!")

