import unittest
from unittest.mock import patch
from homework import calculate_team_effort_hours

class TestCalculateTeamEffortHours(unittest.TestCase):

    def test_happy_path(self):
        with patch('builtins.input', side_effect=["5", "3", "2", "1", "2", "3,5", "4,6", "5,7"]):
            with patch('builtins.print') as mock_print:
                calculate_team_effort_hours()
                

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a", "b", "c"]):
            with patch('builtins.print') as mock_print:
                calculate_team_effort_hours()
                

    def test_other_possible_paths(self):
        with patch('builtins.input', side_effect=["5", "3", "2", "1", "2", "3,5", "4,6", "5,7"]):
            with patch('builtins.print') as mock_print:
                calculate_team_effort_hours()
              

if __name__ == '__main__':
    unittest.main()
