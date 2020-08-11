from __future__ import print_function
from datetime import datetime
import yaml
import os

os.chdir(os.path.dirname(__file__))

yaml_file = open("../source/film/screenings.yaml")
screeningsData = yaml.load(yaml_file, Loader=yaml.FullLoader)

#data = sorted(parsed_yaml_file, key = lambda i: (i['screeningDate'], i['screeningCinema'], i['screeningTime']))

calendarData = {}

for s in screeningsData:
    myDate = calendarData.get(s['screeningDate'], dict())
    myCinema = myDate.get(s['screeningCinema'], [])
    myCinema.append({'screeningTime': s['screeningTime'], 'filmTitle': s['filmTitle_et'], 'filmPath': s['filmPath']})
    myCinemaSorted = sorted(myCinema, key = lambda i: (i['screeningTime']))
    #sort kellaajajärgi
    myDate[s['screeningCinema']] = myCinemaSorted
    calendarData[s['screeningDate']] = myDate

with open(r'screeningsCalendar.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(calendarData, file, default_flow_style=False, sort_keys=True, indent=4, allow_unicode=True)

print("fetching screeningsData")

