import datetime
import unittest
from unittest.mock import patch


def print_with_time(*args, **kwargs) -> None:
    """
    Print the given information with the current time in HH:MM:SS format.
    """
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}]", *args, **kwargs)


class TestPrintWithTime(unittest.TestCase):
    @patch("builtins.print")
    @patch("datetime.datetime")
    def test_print_with_time(self, mock_datetime, mock_print):
        """
        Test that this function works correctly by running
        the following command in the terminal:

        time python -m unittest src.utils.print_with_time
        """
        mock_datetime.now.return_value.strftime.return_value = "12:00:00"
        print_with_time("Hello.")
        mock_print.assert_called_with("[12:00:00]", "Hello.")

        mock_datetime.now.return_value.strftime.return_value = "12:00:01"
        print_with_time("Hello", "world.")
        mock_print.assert_called_with("[12:00:01]", "Hello", "world.")

        mock_datetime.now.return_value.strftime.return_value = "12:00:02"
        variable_1 = {"a": 1, "b": 2, "c": 3}
        variable_2 = 123
        variable_3 = 3.14
        variable_4 = "string"
        variable_5 = True
        variable_6 = False
        variable_7 = {1, 2, 3}
        variable_8 = [1, 2, 3]
        variable_9 = (1, 2, 3)
        variable_11 = range(10)
        variable_12 = print
        print_with_time(
            "You can print variables like",
            variable_1,
            variable_2,
            variable_3,
            variable_4,
            variable_5,
            variable_6,
            variable_7,
            variable_8,
            variable_9,
            variable_11,
            "and",
            variable_12,
        )


if __name__ == "__main__":
    unittest.main()
