import unittest
from math_quiz import generate_random_integer, get_random_operation, create_math_problem

class TestMathQuiz(unittest.TestCase):
    
    def test_generate_random_integer(self):
        """Test that generate_random_integer returns a value within the specified range."""
        min_value = 1
        max_value = 10
        result = generate_random_integer(min_value, max_value)
        self.assertGreaterEqual(result, min_value, "Result is below minimum value.")
        self.assertLessEqual(result, max_value, "Result is above maximum value.")

    def test_get_random_operation(self):
        """Test that get_random_operation returns one of the expected operations."""
        operations = ['+', '-', '*']
        result = get_random_operation()
        self.assertIn(result, operations, "Result is not one of the expected operations.")

    def test_create_math_problem(self):
        """Test that create_math_problem correctly formats the problem and calculates the answer."""
        # Test addition
        problem_text, answer = create_math_problem(3, 5, '+')
        self.assertEqual(problem_text, "3 + 5", "Problem text does not match expected format.")
        self.assertEqual(answer, 8, "Answer for addition is incorrect.")

        # Test subtraction
        problem_text, answer = create_math_problem(10, 4, '-')
        self.assertEqual(problem_text, "10 - 4", "Problem text does not match expected format.")
        self.assertEqual(answer, 6, "Answer for subtraction is incorrect.")

        # Test multiplication
        problem_text, answer = create_math_problem(2, 3, '*')
        self.assertEqual(problem_text, "2 * 3", "Problem text does not match expected format.")
        self.assertEqual(answer, 6, "Answer for multiplication is incorrect.")

if __name__ == '__main__':
    unittest.main()
