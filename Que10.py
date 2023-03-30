from datetime import datetime, timedelta

def days_before_date(date_str, n):
    date_format = '%y-%m-%d'
    date = datetime.strptime(date_str, date_format)
    days_delta = timedelta(days=n)
    new_date = date - days_delta
    return new_date.strftime(date_format)

date_str = input("Enter date as dd-mm-yy: ")
n = int(input("Enter days before: "))
print(days_before_date(date_str, n))
