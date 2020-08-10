import yaml
import os
from datetime import datetime

os.chdir(os.path.dirname(__file__))

yaml_file = open("../source/film/screenings.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

#print(parsed_yaml_file)
# print(parsed_yaml_file[0]["screeningEventivalId"])
#parsed_yaml_file.sort()
#sorted(parsed_yaml_file, key = lambda i: i['screeningDate'])
print(parsed_yaml_file)
for val in parsed_yaml_file:
    print(val["screeningDate"])
