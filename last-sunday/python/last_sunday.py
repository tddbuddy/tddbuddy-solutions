from datetime import datetime, timedelta

def last_sunday(year):
    # Check if the input is an integer
    if not isinstance(year, int):
        raise ValueError("The year must be an integer.")

    last_sundays = []
    for month in range(1, 13):
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        last_day_of_month = next_month - timedelta(days=1)

        days_to_subtract = (last_day_of_month.weekday() + 1) % 7
        last_sunday_of_month = last_day_of_month - timedelta(days=days_to_subtract)
        last_sundays.append(last_sunday_of_month.strftime('%Y-%m-%d'))

    return last_sundays

