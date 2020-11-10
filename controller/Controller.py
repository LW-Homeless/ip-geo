from colorama import init, Fore
from model.ConfigFile import ConfigFile
from model.Geolocation import Geolocation
from model.DownloadDb import DownloadDb
from geopy.exc import GeocoderUnavailable
from tabulate import tabulate
import os
import requests


class Controller:

    def __init__(self):
        init()
        self.__update_date = DownloadDb()
        try:
            self.__update_date.get_database()
        except requests.HTTPError as ex:
            print(Fore.RED + "[X] API-KEY Maxmind: " + ex.__str__(), end="\n\n")

    def add_api_key(self):

        key = input("INGRESE API-KEY MAXMIND > ")

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assest", "config.ini")

        api_key = ConfigFile(path)
        api_key.write_file("api-key", "key", key)

    def query_ip(self):
        try:
            ips = input("Ingrese IP o IPs > ")
            print("\n")

            geo_ip = Geolocation(ips)

            for response in geo_ip.get_geo_info():
                print(Fore.RED + "="*55 + response[0][0] + "="*55, end="\n\n")
                print(Fore.RED + "[i] Ubicacion Continental")
                table = response[1]
                print(Fore.GREEN + tabulate(table, headers=["Geoname-id", "Continente"], tablefmt="grid",
                                            colalign=("left",)), end="\n\n")

                print(Fore.RED + "[i] Ubicacion Pais")
                table = response[2]
                print(Fore.GREEN + tabulate(table, headers=["Geoname-id", "Union Europea", "Codigo ISO", "Pais"],
                                            tablefmt="grid", colalign=("left",)), end="\n\n")

                print(Fore.RED + "[i] Ubicacion Ciudad")
                table = response[3]
                print(Fore.GREEN + tabulate(table, headers=["Geoname-id", "Ciudad"], tablefmt="grid",
                                            colalign=("left",)), end="\n\n")

                print(Fore.RED + "[i] Localizacion")
                table = response[4]
                print(Fore.GREEN + tabulate(table, headers=["Direccion", "Latitud", "Longitud", "Zona horaria"],
                                            tablefmt="grid", colalign=("left",)), end="\n\n")

                print(Fore.RED + "[i] Codigo Postal")
                table = response[5]
                print(Fore.GREEN + tabulate(table, headers=["Codigo Postal"], tablefmt="grid", colalign=("left",)),
                      end="\n\n")

                print(Fore.RED + "[i] Otra Informacion")
                table = response[6]
                print(Fore.GREEN + tabulate(table, headers=["ISP", "ASN", "ASO", "Domain", "Direccion IP",
                                                            "Bloque de Red"],
                                            tablefmt="grid", colalign=("left",)), end="\n")

                print(Fore.RED + "=" * 110 + " Fin " + response[0][0], end="\n\n")

        except GeocoderUnavailable as ex:
            print(Fore.YELLOW + "[!] " + ex.__str__())
            exit(0)
        except FileNotFoundError as ex:
            print(Fore.RED + "[X] Base de datos no encontrada")
        except ValueError:
            raise ValueError("La direccion IP no parece ser una direcion IPv4 o IPv6")

    def exit_program(self):
        exit(0)
