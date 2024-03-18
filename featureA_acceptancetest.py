import unittest
from unittest.mock import patch
from homework import calculate_sprint_velocity 

class TestFeatureAAcceptance(unittest.TestCase):

    @patch('builtins.input', side_effect=["10 20 30"])
    @patch('builtins.print')
    def test_calculate_sprint_velocity(self, mock_print, mock_input):
        calculate_sprint_velocity()
        mock_print.assert_called_with("Average sprint velocity: 20.00 points")

    @patch('builtins.input', side_effect=[""])
    @patch('builtins.print')
    def test_empty_input(self, mock_print, mock_input):
        calculate_sprint_velocity()
        mock_print.assert_called_with("No points entered. Please enter the completion points of previous sprints.")

    @patch('builtins.input', side_effect=["abc def"])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input):
        calculate_sprint_velocity()
        mock_print.assert_called_with("Invalid input. Please enter numbers separated by spaces for previous sprint points.")

if __name__ == '__main__':
    unittest.main()

