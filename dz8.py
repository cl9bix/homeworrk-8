from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    next_week = today + timedelta(days=7)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays_per_day = {day: [] for day in days}

    for user in users:
        name = user['name']
        bday = user['birthday'].replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=next_week.year)
        if bday < next_week:
            day_of_week = days[bday.weekday()]
            birthdays_per_day[day_of_week].append(name)

    for day, names in birthdays_per_day.items():
        if names:
            print(f"{day}: {', '.join(names)}")
