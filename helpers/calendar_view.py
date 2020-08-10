from __future__ import print_function
from datetime import datetime
import yaml
import os

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
        # calendarInfo[val["screeningCinema"]].append(val["screeningDate"])


# print(calendarInfo)

testStuff = [{'screeningDate' : '20200202',
                'screeningCinema' :
                    [{'Raekoja plats' :
                        [{'filmSlug' : 'whatever', 'filmName' : 'See on filmi nimi'},
                        {'filmSlug' : 'whatever22', 'filmName' : 'See on filmi ni222mi'}]
                    },
                    {'Mingi plats' :
                        [{'filmSlug' : 'whatever', 'filmName' : 'See on filmi nimi'},
                        {'filmSlug' : 'whatever22', 'filmName' : 'See on filmi ni222mi'}]
                    }]
            },
            {'screeningDate' : '20200205',
                'screeningCinema' :
                    [{'Raekoja plats' :
                        [{'filmSlug' : 'whatever', 'filmName' : 'See on filmi nimi'},
                        {'filmSlug' : 'whatever22', 'filmName' : 'See on filmi ni222mi'}]
                    },
                    {'Mingi plats' :
                        [{'filmSlug' : 'whatever', 'filmName' : 'See on filmi nimi'},
                        {'filmSlug' : 'whatever22', 'filmName' : 'See on filmi ni222mi'}]
                    }]
            }]

# print(testStuff[])

with open(r'testyaml.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(testStuff, file, default_flow_style=False, sort_keys=False, indent=4, allow_unicode=True)

print(testStuff[1]["screeningCinema"][0])


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









