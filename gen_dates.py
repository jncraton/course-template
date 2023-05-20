from dateutil.rrule import rruleset, rrule, WEEKLY, MO, TU, WE, TH, FR
from datetime import datetime
import csv
import json
from itertools import zip_longest

config = json.load(open('config.json'))

day_map = {"M": MO, "T": TU, "W": WE, "R": TH, "F": FR}
lecture_days = [day_map[d] for d in config["lecture_days"]]

rules = rruleset()
rules.rrule(
    rrule(
        WEEKLY,
        dtstart=datetime.fromisoformat(config["start_date"]),
        until=datetime.fromisoformat(config["end_date"]),
        byweekday=lecture_days,
    )
)
for b in config["breaks"]:
    rules.exdate(datetime.fromisoformat(b))

with open('topics.tsv') as f:
    lectures = [r for r in csv.DictReader(f, dialect='excel-tab') if r['type'] != 'lab']

    start_week = None
    last_week = 0

    for i, day in enumerate(zip_longest(rules, lectures)):
        if not start_week:
            start_week = int(day[0].strftime("%V")) - 1

        week = int(day[0].strftime("%V")) - start_week

        if week != last_week:
            last_week = week
        
        print(f"Week {week} Day {i+1:02d} {day[1]['name'] if day[1] != None else 'Out of topics'} ({day[0].strftime('%A, %B %d')})")
