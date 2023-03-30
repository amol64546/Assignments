from datetime import datetime, timedelta

def dates_within_range(from_date, to_date, difference):
    date_format = '%y-%m-%d'
    # Convert the date strings to datetime objects
    from_date = datetime.strptime(from_date, date_format)
    to_date = datetime.strptime(to_date, date_format)
    
    # Calculate the difference between the dates
    delta = abs(from_date - to_date)
    
    # Compare the difference with the input value
    if delta.days < difference:
        return True
    else:
        return False

print("Enter date as dd-mm-yy")
from_date = input("Enter from_date: ")
to_date = input("Enter to_date: ")
difference = int(input("Enter days of difference: "))
print(dates_within_range(from_date,to_date,difference))  
