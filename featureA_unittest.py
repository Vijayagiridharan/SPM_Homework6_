import unittest
from unittest.mock import patch
from homework import calculate_sprint_velocity

class TestCalculateSprintVelocity(unittest.TestCase):

    def test_happy_path(self):
        points_input = "10 20 30"
        expected_output = "Average sprint velocity: 20.00 points"
        with patch('builtins.input', return_value=points_input):
            with patch('builtins.print') as mock_print:
                calculate_sprint_velocity()
                mock_print.assert_called_once_with(expected_output)

    def test_empty_input(self):
        points_input = ""
        expected_output = "No points entered. Please enter the completion points of previous sprints."
        with patch('builtins.input', return_value=points_input):
            with patch('builtins.print') as mock_print:
                calculate_sprint_velocity()
                mock_print.assert_called_once_with(expected_output)

    def test_invalid_input(self):
        points_input = "abc def"
        expected_output = "Invalid input. Please enter numbers separated by spaces for previous sprint points."
        with patch('builtins.input', return_value=points_input):
            with patch('builtins.print') as mock_print:
                calculate_sprint_velocity()
                mock_print.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()
