from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        difference = today - given_date

        return print(difference.days)

    except ValueError:
        return "Несправний формат дати. Використовуйте YYYY-MM-DD."


get_days_from_today("2020-08-03")