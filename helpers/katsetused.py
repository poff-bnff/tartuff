from __future__ import print_function
from datetime import datetime
import yaml
import os

os.chdir(os.path.dirname(__file__))

#data = sorted(parsed_yaml_file, key = lambda i: (i['screeningDate'], i['screeningCinema'], i['screeningTime']))

def compileScreeningsCalendar (source, output):

    yaml_file = open("../source/film/"+source)
    screeningsData = yaml.load(yaml_file, Loader=yaml.FullLoader)

    calendarData = {}
    for s in screeningsData:
        myDate = calendarData.get(s['screeningDate'], dict())
        myCinema = myDate.get(s['screeningCinema'], [])
        #screenings (ilma keele laiendita pidi olema s['filmTitle_et'])
        myCinema.append({'screeningDatetime': s['screeningDatetime'], 'screeningTime': s['screeningTime'], 'filmTitle': s['filmTitle'], 'filmPath': s['filmPath']})
        #sorteerimisel -3h
        myCinemaSorted = sorted(myCinema, key = lambda i: (i['screeningTime']))
        #sort kellaajajärgi
        myDate[s['screeningCinema']] = myCinemaSorted
        calendarData[s['screeningDate']] = myDate

    with open(r'../source/film/'+output, 'w', encoding='utf-8') as file:
        yaml.dump(calendarData, file, default_flow_style=False, sort_keys=True, indent=4, allow_unicode=True)

    print("compailing " + output)

compileScreeningsCalendar('screenings.et.yaml', 'screeningsTEST.yaml')
