from world_map import WorldMap
from city_data import CityData


def test_world_map_init():
    instance = WorldMap()

    assert instance is not None


def test_load_map():
    instance = WorldMap()
    instance.load(".\\resources\\worldcities_countries.csv")

    assert len(instance.cities) == 6

    assert instance.cities['Japan!Tokyo'] == [35.6897, 139.6922]
    assert instance.cities['Indonesia!Jakarta'] == [-6.175, 106.8275]
    assert instance.cities['Japan!Osaka'] == [34.6939, 135.5022]
    assert instance.cities['China!Dezhou'] == [37.436, 116.359]
    assert instance.cities['China!Nanchong'] == [30.8372, 106.1106]
    assert instance.cities['Germany!Berlin'] == [52.5200, 13.4050]


def test_object_convert():
    instance = WorldMap()
    row = "Tokyo,35.6897,139.6922,Japan,JPN,1392685764"
    city = instance.object_convert(row)

    assert isinstance(city, CityData) is True
    assert isinstance(city, WorldMap) is False
    assert type(city) != object


def test_country_city_key():
    city = CityData('Tokyo', '35.6897', '139.6922', 'Japan', 'JPN')
    instance = WorldMap()

    assert instance.country_city_key(city) == ('Japan!Tokyo', [35.6897, 139.6922])
    assert instance.country_city_key(city) != ('Bangladesh!Jakarta', [-6.175, 106.8275])
    assert instance.country_city_key(city) != object


def test_search_func():
    world_map = WorldMap()
    world_map.load(".\\resources\\worldcities_countries.csv")
    result = world_map.search('Japan', 'Tokyo')
    assert result == (35.6897, 139.6922)

    result = world_map.search('Chebiy', 'Lulumba')
    assert result == (0, 0)
