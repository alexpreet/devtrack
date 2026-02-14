from collections import defaultdict
from storage import load_data


def total_hours():
    data = load_data()
    return sum(entry["hours"] for entry in data)


def unique_skills():
    data = load_data()
    return len(set(entry["skill"] for entry in data))


def skill_distribution():
    data = load_data()
    skill_hours = defaultdict(float)

    for entry in data:
        skill_hours[entry["skill"]] += entry["hours"]

    sorted_data = sorted(skill_hours.items(), key=lambda x: x[1], reverse=True)

    skills = [item[0] for item in sorted_data]
    hours = [item[1] for item in sorted_data]

    return skills, hours


def daily_trend():
    data = load_data()
    daily_hours = defaultdict(float)

    for entry in data:
        daily_hours[entry["date"]] += entry["hours"]

    sorted_data = sorted(daily_hours.items())

    dates = [item[0] for item in sorted_data]
    hours = [item[1] for item in sorted_data]

    return dates, hours


def productivity_score():
    return round((total_hours() * 2) + (unique_skills() * 5), 2)
