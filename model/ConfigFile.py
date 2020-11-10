from configparser import ConfigParser
from configparser import NoSectionError
from configparser import NoOptionError
from model.ConfigFileException import ConfigFileException
import os


class ConfigFile:

    def __init__(self, path):
        self.__path = path
        self.__parse = ConfigParser()

    def read_file(self, section, key):
        try:

            self.__parse.read(self.__path)
            return self.__parse.get(section, key)

        except NoSectionError:
            raise ConfigFileException("Seccion no encontrada")
        except NoOptionError:
            raise ConfigFileException("Clave no encontrada en la seccion especificada")
        except Exception:
            raise ConfigFileException("Se producido un error al acceder al archivo de configuracion")

    def write_file(self, section, key, value):
        try:
            self.__parse.read(self.__path)
            self.__parse.set(section, key, value)

            if os.path.exists(self.__path):
                with open(self.__path, "wt") as file:
                    self.__parse.write(file)
                    file.close()
            else:
                raise ConfigFileException("No se pudo acceder al archivo de configuracion")
        except NoSectionError:
            raise ConfigFileException("Seccion no encontrada")
        except NoOptionError:
            raise ConfigFileException("Clave no encontrada en la seccion especificada")
        except ConfigFileException:
            raise ConfigFileException
        except Exception:
            raise ConfigFileException("Se producido un error al acceder al archivo de configuracion")
