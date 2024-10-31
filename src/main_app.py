from distance_calculator import *
from world_map import *
from user_interface import UserInterface

if __name__ == '__main__':
    print("Hello, welcome to our distance city calculator!")

    calculator = DistanceCalculator()
    world_map = WorldMap()
    world_map.load(".\\resources\\worldcities_countries.csv")
    user_interface = UserInterface()

    while True:
        # source, destination = user_interface.take_partial_user_input(world_map)
        #
        # source_coordinate, destination_coordinate = user_interface.normalize_user_input(source, destination, world_map)
        # source_coordinate, destination_coordinate, source, destination = user_interface.take_user_input(world_map)
        source_destination_dto = user_interface.take_user_input(world_map)
        distance = calculator.calculate_distance((source_destination_dto.get_source_coordinate().get_latitude(),
                                                  source_destination_dto.get_source_coordinate().get_longitude()),
                                                 (source_destination_dto.get_destination_coordinate().get_latitude(),
                                                  source_destination_dto.get_destination_coordinate().get_longitude()))
        print(f"the distance between {source_destination_dto.get_source()} and {source_destination_dto.get_destination()} is {distance} km")
        if user_interface.check_for_exit() is True:
            break
