from datetime import datetime, date


def day_of_year(user_date):
    """user_date in form Y-M-D"""
    user_date = user_date.replace("-", "")
    date_obj = datetime.strptime(user_date, "%Y%m%d").date()
    day_of_year = date_obj.timetuple().tm_yday
    return day_of_year
