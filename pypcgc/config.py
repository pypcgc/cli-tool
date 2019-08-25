import os
import yaml

CONFIG_FILE_PATH = '{0}/.pypcgc.yaml'.format(os.path.expanduser("~"))

class Config:
    def __init__(self):
        self.exist = os.path.isfile(CONFIG_FILE_PATH)
        if self.exist:
            self._config = yaml.load(open(CONFIG_FILE_PATH, 'r').read(),
            Loader=yaml.loader.FullLoader)

        else:
            self._config = {}

    def read(self):
        return self._config

    def write(self):
        if self._config is not {}:
            open(CONFIG_FILE_PATH, 'w'
                ).write(yaml.dump(self._config, default_flow_style=False))

    def set_to_config(self, group, key, value):
        try:
            self._config[group].update({key: value})
        except Exception:
            self._config.update({group: {key: value}})
