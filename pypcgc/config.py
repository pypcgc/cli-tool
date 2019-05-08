import os


CONFIG_FILE_PATH = "{0}/.pypcgc".format(os.path.expanduser("~"))

def exists():
    return os.path.isfile(CONFIG_FILE_PATH)

def write(value):
    if not exists():
        open(CONFIG_FILE_PATH, "w")

    config_file_lines = open(CONFIG_FILE_PATH).readlines()

    atributes = value.split("=")
    position = 0
    found = False

    for line in config_file_lines:
        if atributes[0] in line:
            config_file_lines[position] = value + "\n"
            found = True
        position += 1

    if not found:
        config_file_lines.append(value + "\n")

    open(CONFIG_FILE_PATH, "w").writelines(config_file_lines)

def read():
    config_file_lines = open(CONFIG_FILE_PATH).readlines()
    config = {}

    for line in config_file_lines:
        atribute = line.split("=")
        config[atribute[0]] = atribute[1][:-1]

    return config

