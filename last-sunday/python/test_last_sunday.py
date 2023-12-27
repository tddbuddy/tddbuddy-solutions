import pytest
from last_sunday import last_sunday

@pytest.mark.parametrize("year, expected", [
    # Leap year
    (2024, ['2024-01-28', '2024-02-25', '2024-03-31', '2024-04-28', '2024-05-26', 
            '2024-06-30', '2024-07-28', '2024-08-25', '2024-09-29', '2024-10-27', 
            '2024-11-24', '2024-12-29']),
    # Earliest year possible
    (1, ['0001-01-28', '0001-02-25', '0001-03-25', '0001-04-29', '0001-05-27', 
         '0001-06-24', '0001-07-29', '0001-08-26', '0001-09-30', '0001-10-28', 
         '0001-11-25', '0001-12-30']),
    # Latest year possible
    (9999, ['9999-01-25', '9999-02-22', '9999-03-29', '9999-04-26', '9999-05-31', 
            '9999-06-28', '9999-07-26', '9999-08-30', '9999-09-27', '9999-10-25', 
            '9999-11-29', '9999-12-27']),
])

def test_last_sunday(year, expected):
    assert last_sunday(year) == expected

