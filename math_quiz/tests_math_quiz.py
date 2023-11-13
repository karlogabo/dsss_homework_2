import unittest
from math_quiz import random_integer, random_operator, random_operation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        valid_operators = ["+", "-", "*"]
        operator = random_operator()
        self.assertTrue(operator in valid_operators)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (22, 15, '-', '22 - 15', 7),
                (5, 2, '*', '5 * 2', 10),
                (33.1, 2, '+', '33 + 2', 35),
                (9, 2.2, '*', '9 * 2', 18)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                obtained_problem, obtained_answer = random_operation(num1, num2, operator)
                self.assertTrue(expected_problem == obtained_problem)
                self.assertTrue(expected_answer == obtained_answer)

if __name__ == "__main__":
    unittest.main()
