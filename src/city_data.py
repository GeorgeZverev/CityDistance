class CityData:

    def __init__(self, name: str, latitude: str, longitude: str, country: str, iso_code: str):
        self.__city_name = name
        self.__lat = latitude
        self.__lng = longitude
        self.__country_name = country
        self.__iso = iso_code

    @property
    def city_name(self):
        return self.__city_name

    @city_name.setter
    def city_name(self, name):
        self.__city_name = name

    @property
    def lat(self):
        return float(self.__lat)

    @lat.setter
    def lat(self, latitude):
        self.__lat = latitude

    @property
    def lng(self):
        return float(self.__lng)

    @lng.setter
    def lng(self, longitude):
        self.__lng = longitude

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, country):
        self.__country_name = country

    @property
    def iso(self):
        return self.__iso

    @iso.setter
    def iso(self, iso_code):
        self.__iso = iso_code

    def __str__(self):
        return f"1: {self.__city_name}, 2: {self.lat}, 3: {self.__lng}, 4: {self.__country_name}, 5: {self.__iso}"
