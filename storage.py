import json
import os
from datetime import date

DATA_FILE = "data.json"


def initialize():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def load_data():
    initialize()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def normalize_skill(skill):
    return skill.strip().title()


def add_entry(hours, skill, project):
    if hours <= 0:
        raise ValueError("Hours must be positive")

    skill = normalize_skill(skill)

    data = load_data()

    entry = {
        "date": str(date.today()),
        "hours": float(hours),
        "skill": skill,
        "project": project.strip()
    }

    data.append(entry)
    save_data(data)


def reset_data():
    save_data([])
