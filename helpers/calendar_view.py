import yaml
import os

# os.chdir(os.path.dirname(__file__))

print("current working dir is: " + os.getcwd())
print("current working dir is: " + os.getcwd() +"/source/film/screenings.yaml")

yaml_file = open(os.getcwd() +"/source/film/screenings.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(parsed_yaml_file)
