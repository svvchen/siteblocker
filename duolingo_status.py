import duolingo
import time
from datetime import datetime
import secrets

# tests
# -----
# create an instance of duolingo, pass it auth
# print(secrets.username)
lingo = duolingo.Duolingo(secrets.username, secrets.password)

# set your daily goal
# daily_goal = 10
# -----

def check_goal_reached(duolingo, goal):

    xp_json = duolingo.get_daily_xp_progress()
    lessons_blob = xp_json['lessons_today']

    lesson_xp = 0
    current_date = datetime.today().date()

    # duolingo's api endpoints return xp & lessons strangely
    # xp & lessons carry over from previous days until a new
    # lesson is completed, thus the below date validation

    for lesson in lessons_blob:
        lesson_localized_date = datetime.fromtimestamp(lesson['time']).date()

        if lesson_localized_date == current_date:
            lesson_xp += lesson['xp']

    print(lesson_xp)

    if lesson_xp > goal:
        return True
    else:
        return False

# tests
# -----
# print(check_goal_reached(lingo, daily_goal))
# print(lingo.get_daily_xp_progress())
# -----
