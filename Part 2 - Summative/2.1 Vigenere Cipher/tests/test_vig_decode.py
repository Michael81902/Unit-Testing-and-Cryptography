from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigDecode(TestCase):
    def test_vig_decode(self):
        text = "POMUNHDXOZCVG"
        keyword = "WHIT"
        self.assertEqual(vig_decode(text, keyword), "THEBRAVESSUCK")

    def test_vig_capitalize(self):
        text