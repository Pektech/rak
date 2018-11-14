from datetime import datetime, date
from app.data import christmas_calendar


def day_of_year(user_date):
    """user_date in form Y-M-D"""
    user_date = user_date.replace("-", "")
    date_obj = datetime.strptime(user_date, "%Y%m%d").date()
    day_of_year = date_obj.timetuple().tm_yday
    return str(day_of_year)


def create_date_obj(user_date):
    user_date = user_date.replace("-", "")
    date_obj = datetime.strptime(user_date, "%Y%m%d").date()
    return date_obj


def display_date(user_date_obj):
    day_suffix = get_ordinal(user_date_obj.day)
    # display_date = date_obj.strftime("%A") + ' the ' + day_suffix + ' of ' + date_obj.strftime("%B")
    display_date = f'{user_date_obj.strftime("%A")} the {day_suffix} of {user_date_obj.strftime("%B")}'

    return display_date


def get_ordinal(num):
    return str(num) + (
        "th"
        if 4 <= num % 100 <= 20
        else {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    )


def get_rak_of(_day_of_year):
    rak = christmas_calendar[_day_of_year]
    return rak
