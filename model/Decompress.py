import tarfile
import os
import shutil


class Decompress:

    def __init__(self, path, compressed_file_name, database_name):
        self.__path = path
        self.__file = compressed_file_name  # GeoLite2-City.tar.gz
        self.__db = database_name  # GeoLite2-City.mmdb

    def decompress(self):
        try:
            # Set pointer to current directory
            os.chdir(self.__path)

            # Unzip the file (GeoLite2-City.tar.gz) to get the database
            with tarfile.open(self.__file, 'r') as tar_file:
                tar_file.extractall(self.__path)

                # Get root file to get database (GeoLite2-City_aaaammdd)
                folder = tar_file.getnames()[0]

                # Changing to the root folder (GeoLite2-City_aaaammdd)
                os.chdir(os.path.join(self.__path, folder))

                # copying the database to the assets directory
                shutil.copy(self.__db, self.__path)
                os.chdir(self.__path)

                # Removing the folder (GeoLite2-City_aaaammdd)
                shutil.rmtree(folder)
            tar_file.close()

            os.remove(self.__file)
        except FileNotFoundError:
            raise FileNotFoundError("El sistema no puede encontrar el archivo especificado")
        except tarfile.ReadError:
            raise tarfile.ReadError("El archivo no se pudo abrir correctamente")
