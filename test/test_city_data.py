import pytest
from city_data import CityData


def test_city_data_init():
    instance = CityData("Moscow", "55.7558", "37.6172", "Russia", "RUS")

    assert instance is not None
    assert instance.city_name == "Moscow"
    assert instance.lat == 55.7558
    assert instance.lng == 37.6172
    assert instance.country_name == "Russia"
    assert instance.iso == "RUS"


def test_print_city_data():
    instance = CityData("Moscow", "55.7558", "37.6172", "Russia", "RUS")
    assert instance.__dict__ == {'_CityData__city_name': 'Moscow', '_CityData__lat': '55.7558', '_CityData__lng': '37.6172', '_CityData__country_name': 'Russia', '_CityData__iso': 'RUS'}

