import yaml
import os
from datetime import datetime

os.chdir(os.path.dirname(__file__))

yaml_file = open("../source/film/screenings.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

#print(parsed_yaml_file)
# print(parsed_yaml_file[0]["screeningEventivalId"])

date=''
calendarInfo=[]
#films: list of dictionarys
#ScreeningCinema: list
for val in sorted(parsed_yaml_file, key = lambda i: i['screeningDate']):
    if date != val["screeningDate"]:
        date=(val["screeningDate"])
        calendarInfo.append({'screeningDate' : date})

print(calendarInfo)




