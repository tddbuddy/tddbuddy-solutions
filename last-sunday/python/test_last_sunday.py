import pytest
from last_sunday import last_sunday

@pytest.mark.parametrize("year, expected", [
    (2013, ['2013-01-27', '2013-02-24', '2013-03-31', '2013-04-28', '2013-05-26', 
            '2013-06-30', '2013-07-28', '2013-08-25', '2013-09-29', '2013-10-27', 
            '2013-11-24', '2013-12-29']),
    (2020, ['2020-01-26', '2020-02-23', '2020-03-29', '2020-04-26', '2020-05-31', 
            '2020-06-28', '2020-07-26', '2020-08-30', '2020-09-27', '2020-10-25', 
            '2020-11-29', '2020-12-27']),
    (2032, ['2032-01-25', '2032-02-29', '2032-03-28', '2032-04-25', '2032-05-30', 
            '2032-06-27', '2032-07-25', '2032-08-29', '2032-09-26', '2032-10-31', 
            '2032-11-28', '2032-12-26'])
])
def test_last_sunday(year, expected):
    assert last_sunday(year) == expected


def test_last_sunday_invalid_input():
    with pytest.raises(ValueError):
        last_sunday("not an integer")
