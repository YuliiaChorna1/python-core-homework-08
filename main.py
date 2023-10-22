from datetime import date, timedelta, datetime
from collections import defaultdict

def get_period(start_date: date, days: int):
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(days=1)
    return result

def get_valid_workday(initial_date: date, period: dict) -> str:
    workday = ""    

    while initial_date.weekday() > 4:
        initial_date += timedelta(days=1)

    date_bd = initial_date.day, initial_date.month
    if date_bd in list(period):
        workday = initial_date.strftime("%A")
    return workday
    
        
def get_birthdays_per_week(users: list) -> list:
    start_date = date.today()
    period = get_period(start_date, 7)
    
    birthdays_per_week = defaultdict(list)

    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        
        if date_bd in list(period):
            bd = bd.replace(year=period[date_bd])
            workday = get_valid_workday(bd, period)
            if workday:
                birthdays_per_week[workday].append(user["name"])
                            
    return dict(birthdays_per_week)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
