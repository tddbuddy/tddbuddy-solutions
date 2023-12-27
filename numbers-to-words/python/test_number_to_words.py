import pytest
from number_to_words import number_to_words

def test_single_digits():
    assert number_to_words(0) == "zero"
    assert number_to_words(5) == "five"
    assert number_to_words(8) == "eight"

def test_double_digits():
    assert number_to_words(10) == "ten"
    assert number_to_words(21) == "twenty-one"
    assert number_to_words(77) == "seventy-seven"

def test_three_digits():
    assert number_to_words(100) == "one hundred"
    assert number_to_words(303) == "three hundred three"
    assert number_to_words(555) == "five hundred fifty-five"

def test_four_digits():
    assert number_to_words(2000) == "two thousand"
    assert number_to_words(3466) == "three thousand four hundred sixty-six"
    assert number_to_words(2400) == "two thousand four hundred"
    assert number_to_words(5300) == "five thousand three hundred"

def test_boundary_values():
    assert number_to_words(20) == "twenty"
    assert number_to_words(99) == "ninety-nine"
    assert number_to_words(100) == "one hundred"
    assert number_to_words(999) == "nine hundred ninety-nine"
    assert number_to_words(1000) == "one thousand"
    assert number_to_words(9999) == "nine thousand nine hundred ninety-nine"

def test_special_cases():
    assert number_to_words(11) == "eleven"
    assert number_to_words(12) == "twelve"
    assert number_to_words(13) == "thirteen"

def test_zeros():
    assert number_to_words(1010) == "one thousand ten"
    assert number_to_words(1001) == "one thousand one"

def test_extreme_cases():
    assert number_to_words(1) == "one"
    assert number_to_words(9999) == "nine thousand nine hundred ninety-nine"

def test_invalid_input():
    with pytest.raises(ValueError):
        number_to_words(-1)
    with pytest.raises(ValueError):
        number_to_words(10000)
    with pytest.raises(TypeError):
        number_to_words("one thousand")
