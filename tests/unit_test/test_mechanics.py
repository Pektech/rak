import pytest
from app.mechanics import day_of_year, create_date_obj, display_date

"""2018-12-18 = 352, december , Tuesday
    2018-7-23 = 204, july, Monday
    2018-4-1 = 91, april , sunday"""


@pytest.mark.parametrize(
    "test_date, expected", [("2018-12-18", 352), ("2018-7-2", 183), ("2018-4-1", 91)]
)
def test_day_of_year(test_date, expected):
    assert day_of_year(test_date) == expected


@pytest.mark.parametrize(
    "test_date, expected_day, expected_month",
    [
        ("2018-12-18", "Tuesday", "December"),
        ("2018-7-2", "Monday", "July"),
        ("2018-4-1", "Sunday", "April"),
    ],
)
def test_date_object(test_date, expected_day, expected_month):
    date_obj = create_date_obj(test_date)
    assert date_obj.strftime("%A") == expected_day
    assert date_obj.strftime("%B") == expected_month


@pytest.mark.parametrize(
    "test_date, expected_display",
    [
        ("2018-12-18", "Tuesday the 18th of December"),
        ("2018-7-2", "Monday the 2nd of July"),
        ("2018-4-1", "Sunday the 1st of April"),
    ],
)
def test_display_date(test_date, expected_display):
    test_date = create_date_obj(test_date)
    assert display_date(test_date) == expected_display
