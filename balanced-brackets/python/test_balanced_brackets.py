import pytest
from balanced_brackets import BalancedBrackets

class TestBalancedBrackets:
    """
    Partitions and Boundaries to be tested:

    Empty String
    Balanced Brackets
     Simple []
     Multiple [][]
     Nested [[]]
     Complex Nested [[[][]]]
    Unbalanced Brackets
     Simple ][
     Multiple ][][
     Balanced and unbalanced mix [][]][
     Nested unbalanced [[]][[[]]
    """

    def test_empty_string(self):
        # Arrange
        input = ""

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert result

    def test_simple_balanced_brackets(self):
        # Arrange
        input = "[]"

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert result

    def test_multiple_balanced_pairs(self):
        # Arrange
        input = "[][]"

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert result

    def test_nested_balanced_pairs(self):
        # Arrange
        input = "[[]]"

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert result

    def test_complex_nested_balanced_pairs(self):
        # Arrange
        input = "[[[][]]]"

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert result

    def test_simple_unbalanced_brackets(self):
        # Arrange
        input = "]["

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert not result

    def test_multiple_unmatched_closing_brackets(self):
        # Arrange
        input = "][]["

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert not result

    def test_balanced_pairs_followed_by_unmatched_closing_brackets(self):
        # Arrange
        input = "[][]]["

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert not result

    def test_nested_unbalanced_brackets(self):
        # Arrange
        input = "[[]][[[]"

        # Act
        result = BalancedBrackets().is_balanced(input)

        # Assert
        assert not result

