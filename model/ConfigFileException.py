class ConfigFileException(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = 'Error al ejecutar ConfigFile class'

        super(ConfigFileException, self).__init__(msg)