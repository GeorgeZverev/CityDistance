from global_coordinate import GlobalCoordinate
from world_map import WorldMap
from source_destination_dto import SourceDestinationDto


class UserInterface:
    def take_user_input(self, world_map: WorldMap) -> SourceDestinationDto:
        source, destination = self.take_partial_user_input(world_map)

        source_coordinate, destination_coordinate = self.normalize_user_input(source, destination, world_map)

        return SourceDestinationDto(source_coordinate, destination_coordinate, source, destination)

    def take_partial_user_input(self, world_map: WorldMap) -> (str, str):
        partial_source_letters = input("1.Enter first 3 letters of source city: ")
        source = self.__find_city(partial_source_letters, world_map)
        partial_destination_letters = input("2.Enter first 3 letters of source city: ")
        destination = self.__find_city(partial_destination_letters, world_map)
        return source, destination

    def __find_city(self, partial_city_letters: str, world_map: WorldMap) -> str:
        potential_cities = self.__find_potential_cities(partial_city_letters, world_map)

        self.__print_potential_selections(potential_cities)

        if not potential_cities:
            print('You misspelled!')
            exit()

        number = input("\nSelect a number: ")
        for city in potential_cities:
            if number in city:
                city = self.__remove_leading_number(city)
                return city
            #     city = ' '.join([integer for integer in city if not integer.isdigit()])
            #     print(city)
            #     city = city.replace(' ', '')
            #     return city
        print('You selected non-existing number!')
        exit()

    @staticmethod
    def __find_potential_cities(partial_city_letters: str, world_map: WorldMap) -> []:
        partial_city_letters = '!' + partial_city_letters
        index = 1
        potential_cities = []
        for keys in world_map.cities.keys():
            if partial_city_letters in keys:
                key = f"{index} {keys}"
                key = key.replace('!', ',')
                potential_cities.append(key)
                index += 1
        return potential_cities

    @staticmethod
    def __print_potential_selections(potential_cities: list):
        for cities in potential_cities:
            print(cities)

    @staticmethod
    def __remove_leading_number(city: str) -> str:
        list_of_tokens = city.split(' ')
        normalized_city = ''
        for index, token in enumerate(list_of_tokens):
            if index == 0:
                continue
            normalized_city = normalized_city + token + ' '
        normalized_city = normalized_city.rstrip()
        return normalized_city

    @staticmethod
    def normalize_user_input(source: str, destination: str, world_map: WorldMap) -> (GlobalCoordinate, GlobalCoordinate):
        latitude, longitude = world_map.search(source.split(',')[0], source.split(',')[1])
        source_coordinate = GlobalCoordinate(latitude, longitude)
        # source_coordinate_1, source_coordinate_2 = world_map.search(source.split(',')[0], source.split(',')[1])
        latitude, longitude = world_map.search(destination.split(',')[0], destination.split(',')[1])
        destination_coordinate = GlobalCoordinate(latitude, longitude)
        # destination_coordinate_1, destination_coordinate_2 = world_map.search(destination.split(',')[0], destination.split(',')[1])
        return source_coordinate, destination_coordinate

    @staticmethod
    def check_for_exit() -> bool:
        response = input("Do you want to proceed? (y/n) ")
        if response == 'y':
            return False
        else:
            return True
