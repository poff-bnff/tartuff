import yaml
import os
from datetime import datetime

os.chdir(os.path.dirname(__file__))

yaml_file = open("../source/film/screenings.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

#print(parsed_yaml_file)
#print(parsed_yaml_file[0]["screeningEventivalId"])
# kuupäev selle all selle päeva seanside kinod ja selle all selle päeva selle kino kõik seansid ajalises järjekorras
date=''
calendarInfo=[]
screeningPlace=''
for val in sorted(parsed_yaml_file, key = lambda i: i['screeningDate']):

    if date != val["screeningDate"]:
        date=(val["screeningDate"])
        calendarInfo.append({'screeningDate' : date})
        screeningPlace=val["screeningCinema"]
        calendarInfo.append({'screeningCinema' : {screeningPlace}})



print(calendarInfo)


#     cinema=''
 #       for val in sorted(parsed_yaml_file, key = lambda i: i['screeningCinema']):
  #          if cinema != val["screeningCinema"]:
 #               cinema=(val["screeningCinema"])
#                print(calendarInfo)
 #               print(cinema)
 #               calendarInfo["screeningCinema"] = { "tartu kino", "pärnu kino"}
#



#cinema=''
#for val in sorted(parsed_yaml_file, key = lambda i: i['screeningCinema']):
#    if cinema != val["screeningCinema"]:
#        cinema=(val["screeningCinema"])









