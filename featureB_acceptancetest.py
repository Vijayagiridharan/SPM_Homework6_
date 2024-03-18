import unittest
from unittest.mock import patch
from homework import calculate_team_effort_hours

class TestFeatureBAcceptance(unittest.TestCase):
    @patch('builtins.input', side_effect=["5", "3", "2", "1", "2", "3,5", "4,6", "5,7"])
    @patch('builtins.print')
    def test_calculate_team_effort_hours(self, mock_print, mock_input):
        calculate_team_effort_hours()
        mock_print.assert_called()  

if __name__ == '__main__':
    unittest.main()
