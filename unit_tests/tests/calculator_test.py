from unittest import TestCase, main
from unit_tests.calculator import calculator


# тесты пишутся как методы класса
class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("3-1"), 2)

    def test_multi(self):
        self.assertEqual(calculator("4*4"), 16)

    def test_devide(self):
        self.assertEqual(calculator("10/5"), 2.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("abracadabra")
        self.assertEqual(
            "Выражение должно содержать хотя бы 1 знак +-/*", e.exception.args[0]
        )

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2+2")
        self.assertEqual(
            "Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0]
        )

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2*5")
        self.assertEqual(
            "Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0]
        )

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator("2.2+3.0")
        self.assertEqual(
            "Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0]
        )

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator("a+b")
        self.assertEqual(
            "Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0]
        )


# запускать так python -m unit_tests.tests.calculator_test
if __name__ == "__main__":
    main()
