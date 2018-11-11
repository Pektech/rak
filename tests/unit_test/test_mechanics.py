import pytest
from app.mechanics import day_of_year


@pytest.mark.parametrize(
    "test_date, expected", [("2018-12-18", 352), ("2018-7-23", 204), ("2018-4-1", 91)]
)
def test_day_of_year(test_date, expected):
    assert day_of_year(test_date) == expected
