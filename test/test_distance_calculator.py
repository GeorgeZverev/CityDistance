from distance_calculator import DistanceCalculator
from world_map import WorldMap


def test_distance_calculator():
    calculator = DistanceCalculator()

    assert calculator is not None


# def test_distance_calculate():
#     calculator = DistanceCalculator()
#     assert calculator.calculate_distance((100, 10), (10, 100)) == 8912.9


def test_end_to_end():
    world_map = WorldMap()
    world_map.load(".\\test\\resources\\worldcities_countries.csv")
    city_one_coordinates = world_map.search('Japan', 'Tokyo')
    city_two_coordinates = world_map.search('Indonesia', 'Jakarta')

    calculator = DistanceCalculator()

    assert calculator.calculate_distance(city_one_coordinates, city_two_coordinates) == 5783.7


def test_corner_cases():
    calculator = DistanceCalculator()
    assert calculator.calculate_distance((100, 10), (10, 100)) == 8912.9

    assert calculator.calculate_distance((0, 0), (0, 0)) == 0

    assert calculator.calculate_distance((1000, 10), (-10, -1000)) == 0

    assert calculator.calculate_distance((100, 10000), (-100000, -1000000)) == 0


