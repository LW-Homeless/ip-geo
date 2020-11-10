from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import geoip2.database
import os


class Geolocation:

    def __init__(self, ip):
        self.__ip = ip
        self.__continent = ''
        self.__country = ''
        self.__city = ''
        self.__location = ''
        self.__postal_code = ''
        self.__traits = ''
        self.__reader = geoip2.database.Reader(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                            "assest", "GeoLite2-City.mmdb"))

    def get_geo_info(self):
        try:
            response = self.__reader.city(self.__ip)

            self.__continent = [response.continent.geoname_id, response.continent.names["es"]]

            self.__country = [response.country.geoname_id, response.country.is_in_european_union,
                              response.country.iso_code, response.country.names["es"]]

            self.__city = [response.city.geoname_id, response.city.name]

            self.__location = [response.location.latitude, response.location.longitude, response.location.time_zone]

            geolocator = Nominatim(user_agent='IPGeo')

            location = geolocator.reverse(str(self.__location[0]) + "," + str(self.__location[1]))

            address = location.raw["address"]["road"] if "road" in location.raw["address"] else ""
            address += " " + location.raw["address"]["house_number"] if "house_number" in location.raw["address"] else ""
            address += " " + location.raw["address"]["city"] if "city" in location.raw["address"] else ""
            address += " " + location.raw["address"]["county"] if "county" in location.raw["address"] else ""
            address += " Cod.Postal: " + location.raw["address"]["postcode"] if "postcode" in location.raw["address"] else ""

            self.__location.insert(0, address)

            self.__postal_code = [response.postal.code]

            self.__traits = [response.traits.isp, response.traits.autonomous_system_number,
                             response.traits.autonomous_system_organization, response.traits.domain,
                             response.traits.ip_address, response.traits.network]

            yield [[self.__ip], [self.__continent], [self.__country], [self.__city], [self.__location],
                   [self.__postal_code], [self.__traits]]

            self.__reader.close()
        except GeocoderUnavailable:
            raise GeocoderUnavailable("No se pudo establecer conexion, compruebe su conexion a internet")
        except FileNotFoundError:
            raise FileNotFoundError("[X] Base de dato no encontrada")
