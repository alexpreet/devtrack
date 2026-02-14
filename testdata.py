import random
from datetime import datetime, timedelta
from storage import save_data

SKILLS = ["Python", "Machine Learning", "SQL", "UI", "DSA", "API"]


def generate_test_data():
    data = []
    today = datetime.today()

    for i in range(30):
        date = today - timedelta(days=i)

        for _ in range(random.randint(1, 3)):
            skill = random.choices(
                SKILLS,
                weights=[40, 15, 15, 10, 10, 10]
            )[0]

            entry = {
                "date": str(date.date()),
                "hours": round(random.uniform(0.5, 4), 1),
                "skill": skill,
                "project": "Practice"
            }

            data.append(entry)

    save_data(data)
