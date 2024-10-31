from city_data import CityData
from my_error import MyError


class WorldMap:

    def __init__(self):
        self.__cities = {}

    @property
    def cities(self):
        return self.__cities

    def load(self, location: str):
        with open(location, encoding='utf-8') as f:
            rows = f.read().split("\n")
            for row in rows:
                if row.startswith('city') is True:
                    continue
                city = self.object_convert(row)
                city_key, city_value = self.country_city_key(city)
                self.__cities[city_key] = city_value

    def object_convert(self, row: str) -> CityData:
        elements = row.split(',')
        city = CityData(elements[0], elements[1], elements[2], elements[3], elements[4])
        return city

    def country_city_key(self, city: CityData):
        key = f'{city.country_name}!{city.city_name}'
        city_list = [city.lat, city.lng]
        return key, city_list

    def search(self, country: str, city: str) -> (float, float):
        key = f'{country.strip()}!{city.strip()}'
        try:
            value = self.__cities[key]
            return value[0], value[1]
        except KeyError:
            return 0, 0

    # def user_input(self):
    #     first_city = ''
    #     second_city = ''
    #     for key, value in self.__cities.items():
    #         if self.__first_city in key:
    #             first_city = value
    #         elif self.__second_city in key:
    #             second_city = value
    #     return first_city, second_city

    # def make_city_dict(self, city: CityData) -> {}:
    #     city_dict = {}
    #     city_list = [city.lat, city.lng]
    #     city_dict[city.city_name] = city_list
    #     for k, v in self.__cities.items():
    #         key = city.city_name
    #         value = city_list
    #         if k == city.country_name:
    #             v[key] = value
    #             return v
    #     return city_dict


