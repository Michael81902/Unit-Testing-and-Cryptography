from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):
    def test_vig_encode(self):
        text= "THEBRAVESSUCK"
        keyword="WHIT"
        self.assertEqual(vig_encode(text, keyword), "POMUNHDXOZCVG")
    def test_vig_encode4(self):
        text= "ThEBraVESsuCk"
        keyword=("WHIT")
        self.assertEqual(vig_encode(text, keyword), "POMUNHDXOZCVG")
    def test_vig_encode5(self):
        text= "T HE  BR AV ES S U C K "
        keyword=("WHIT")
        self.assertEqual(vig_encode(text, keyword), "P OM  UN HD XO Z C V G ")
    def test_vig_encode6(self):
        text="ThE! Braves! Suck!"
        keyword=("WHIT")
        self.assertEqual(vig_encode(text, keyword), "POM! UNHDXO! ZCVG!")