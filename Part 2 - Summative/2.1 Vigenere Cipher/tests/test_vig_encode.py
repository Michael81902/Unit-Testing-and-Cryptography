from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class test_vig_encode(TestCase):
    def test_vig_encode(self):
        text= "The Braves Suck"
        keyword="Whit"
        self.assertEqual(vig_encode(text, keyword), "pom unhdxo zcvg")