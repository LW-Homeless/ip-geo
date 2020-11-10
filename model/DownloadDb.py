from model.ConfigFile import ConfigFile
from model.Decompress import Decompress
from datetime import datetime, timedelta
from colorama import init, Fore
import requests
import os


class DownloadDb:

    def __init__(self):
        init()
        self.__key = ''
        self.__url = ''
        self.__response = ''

    def get_database(self):
        try:

            if self.__update_mmdb():

                print(Fore.BLUE + "[i] Comprobando actualizaciones...", end="\n\n")

                self.__set_api_key()
                self.__set_url()

                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assest")
                os.chdir(path)

                if self.__update_mmdb():

                    self.__response = requests.get(self.__url, stream=True)

                    if self.__response.status_code != 401:
                        with open('GeoLite2-City.tar.gz', 'wb') as db:
                            for chuck in self.__response.iter_content(chunk_size=1024):
                                if chuck:
                                    db.write(chuck)

                        update_date = datetime.now()
                        update_date = update_date.strftime('%Y%m%d')

                        mmdb_update_date = ConfigFile(os.path.join(path, "config.ini"))
                        mmdb_update_date.write_file('mmdb_update_date', 'date', update_date)

                    else:
                        raise requests.HTTPError('Clave de licencia invalida')

                    unzip_db = Decompress(path, 'GeoLite2-City.tar.gz', 'GeoLite2-City.mmdb')
                    unzip_db.decompress()
        except requests.ConnectionError:
            raise requests.ConnectionError("Se produjo un error de conexion")
        except requests.HTTPError as ex:
            raise requests.HTTPError(ex.__str__())
        except requests.Timeout as ex:
            raise requests.Timeout(ex.__str__())

    def __set_api_key(self):
        key = ConfigFile(os.path.join(os.path.dirname(os.path.dirname(__file__)), "assest", "config.ini"))
        self.__key = key.read_file('api-key', 'key')

    def __set_url(self):
        url = ConfigFile(os.path.join(os.path.dirname(os.path.dirname(__file__)), "assest", "config.ini"))
        self.__url = url.read_file('database-url', 'url')
        self.__url = str(self.__url).replace("YOUR_LICENSE_KEY", self.__key)

    def __update_mmdb(self):
        path = os.path.dirname(os.path.dirname(__file__))
        update = ConfigFile(os.path.join(path, "assest", 'config.ini'))
        stored_date = int(update.read_file('mmdb_update_date', 'date'))
        current_date = (datetime.now() - timedelta(days=7))
        current_date = int(current_date.strftime('%Y%m%d'))

        if current_date > stored_date:
            return True
        else:
            return False
