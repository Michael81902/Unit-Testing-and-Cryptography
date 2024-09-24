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

    def test_vig_decode1(self):
        text = "PoMUNhDXOzCVG"
        keyword = ("WHIT")
        self.assertEqual(vig_decode(text, keyword), "THEBRAVESSUCK")
    def test_vig_decode2(self):
        text = " P OM  UN HD XO Z C V G"
        keyword = ("WHIT")
        self.assertEqual(vig_decode(text, keyword), " T HE  BR AV ES S U C K")