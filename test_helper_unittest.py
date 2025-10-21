import unittest

# Beispielhafte Funktion, die getestet wird
def add_numbers(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add_numbers(-2, 5)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
