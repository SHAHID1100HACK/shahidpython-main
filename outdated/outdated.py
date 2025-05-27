import re

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def month_name_to_number(month_name):
    return months.index(month_name) + 1

def validate_mm_dd_yyyy(date):
    pattern = r"^(\d{1,2})/(\d{1,2})/(\d{4})$"
    match = re.match(pattern, date)
    if match:
        month, day, year = map(int, match.groups())
        return 1 <= month <= 12 and 1 <= day <= 31
    return False

def validate_month_day_year(date):
    pattern = r"^([A-Za-z]+) (\d{1,2}), (\d{4})$"
    match = re.match(pattern, date)
    if match:
        month_name, day, year = match.groups()
        if month_name in months:
            day = int(day)
            return 1 <= day <= 31
    return False

def convert_mm_dd_yyyy_to_iso(date):
    month, day, year = map(int, date.split('/'))
    return f"{year:04d}-{month:02d}-{day:02d}"

def convert_month_day_year_to_iso(date):
    month_name, day, year = re.match(r"^([A-Za-z]+) (\d{1,2}), (\d{4})$", date).groups()
    month_number = month_name_to_number(month_name)
    day = int(day)
    return f"{year}-{month_number:02d}-{day:02d}"

while True:
    user_input = input("Date: ").strip()

    if validate_mm_dd_yyyy(user_input):
        print(convert_mm_dd_yyyy_to_iso(user_input))
        break
    elif validate_month_day_year(user_input):
        print(convert_month_day_year_to_iso(user_input))
        break
