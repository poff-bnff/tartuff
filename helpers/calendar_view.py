import yaml
import os.path

# os.chdir(os.path.dirname(__file__))

yaml_file = open("../source/film/screenings.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(parsed_yaml_file)
