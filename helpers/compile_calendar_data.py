from __future__ import print_function
from datetime import datetime, timedelta
import yaml
import os

#lülitan välja automaatse YAML ankrute genereerimise
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

os.chdir(os.path.dirname(__file__))

#data = sorted(parsed_yaml_file, key = lambda i: (i['screeningDate'], i['screeningCinema'], i['screeningTime']))

#funktsioonid, et teha string kus on dateTime py-le arusaadavaks dateTime-iks ja date-iks
def formatDateTime(dateTime):
    return str(datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S%z'))

def formatedDate(dateTime):
    return str((datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S%z')).date())

yaml_file = open("../source/film/screenings.et.yaml", encoding='utf-8')
screeningsData = yaml.load(yaml_file, Loader=yaml.FullLoader)

calendarDays = []
#screeningData on list of dictionarys
for screening in screeningsData:
    #screening on dictionary tüüpi
    oneDay = []
    for item in calendarDays:
        if item['calendarDate'] == formatedDate(screening['calendarDateTime']):
            #item=[{'calendarDate': '2020-08-10'},]
            oneDay = item
    if oneDay == []:
        calendarDays.append({'calendarDate': formatedDate(screening['calendarDateTime']), 'cinemas': []})
##KAS CALENDARDAY-s PEAKS SORTEERIMA??

#otsin screeningCinemad kuupäeva kaupa välja ja panen objekti sisse
cinemas = []
#see funktsioon, mis määrab, mis järjekorras sorteerime
def keyForSortingCinemas(c):
    sortOrder={"Athena Keskus":0, "Raekoja plats":1, "Elisa Stage":2}
    return sortOrder[c['cinema']]

for day in calendarDays:
    for screening in screeningsData:
        if day['calendarDate'] == formatedDate(screening['calendarDateTime']):
            cinemas.append({'cinema': screening['screeningCinema'], 'screenings': []})
#siin panen cinemas listi day objekti sisse õigesse kohta
#SIIN TAHAN SORTEERIDA
    uniqueCinemas = list({v['cinema']:v for v in cinemas}.values())

    print(sorted(uniqueCinemas, key = keyForSortingCinemas ))
    day['cinemas']=sorted(uniqueCinemas, key = keyForSortingCinemas )

#käin läbi kõik screeningud screenings.yaml failis
for screening in screeningsData:
    [day] = [d for d in calendarDays if d['calendarDate'] == formatedDate(screening['calendarDateTime'])]
    [cinema] = [c for c in day['cinemas'] if c['cinema'] == screening['screeningCinema']]
    cinema['screenings'].append({'filmTitle': screening['filmTitle'], 'screeningTime' : screening['screeningTime'], 'filmPath': screening['filmPath'] })

with open(r'TESTbetter.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(calendarDays, file, default_flow_style=False, sort_keys=True, indent=4, allow_unicode=True, Dumper=NoAliasDumper)


