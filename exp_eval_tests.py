# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval('6 7 8 9 2 3 + 1 - 1 + 4 * 5 / + - + *'), 12)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval('5 1 2 + 4 ** + 3 -'), 83)

    def test_postfix_eval_07(self):
        self.assertRaises(ValueError, postfix_eval, "3 0 /")

    def test_postfix_eval_08(self):
        try:
            postfix_eval("2 3 4 / <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval('4 1 << 2 **'), 64)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix('( 10 + 5 - 7 ) / ( 4 / 2 ) * 2 ** 2'), "10 5 + 7 - 4 2 / / 2 2 ** *")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix('4 << 1 ** 2'), "4 1 << 2 **")

    def test_infix_to_postfix05(self):
        self.assertEqual(infix_to_postfix("( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 )"), "2 3 + 4 * 5 6 - 7 8 + * -")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix01(self):
        self.assertEqual(prefix_to_postfix("+ 3 * 4 5"), "3 4 5 * +")

    def test_prefix_to_postfix02(self):
        self.assertEqual(prefix_to_postfix("/ + 2 3 - + 4 9 - 4 1"), "2 3 + 4 9 + 4 1 - - /")

    #def test_prefix_to_postfix03(self):
       # self.assertEqual(prefix_to_postfix("+ * 3 ** 4 6 ** * 2 / 5 6 8"), "3 4 6 ** * 2 5 6 / 8 ** * +")


    
if __name__ == "__main__":
    unittest.main()
