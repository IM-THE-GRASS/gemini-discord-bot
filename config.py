import json
config_file = open("configs.json")
config = json.loads(config_file.read())
config_file.close
def get_config(item):
    return config[item]