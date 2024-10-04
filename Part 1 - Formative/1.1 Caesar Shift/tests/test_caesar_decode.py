from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import caesar_decode

class TestCaesarDecode(TestCase):
    def test_decode(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI",  5) , "HELLOWORLD" )
    def test_decode1(self):
        self.assertEqual(caesar_decode("mJqqTBTwqI", 5) , "HELLOWORLD")
    def test_decode2(self):
        self.assertEqual(caesar_decode("MJ!QQTBT!!WQI", 5),"HE!LLOWO!!RLD")
    def test_decode3(self):
        self.assertEqual(caesar_decode("MJQQT BTWQI",  5) , "HELLO WORLD" )