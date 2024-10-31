from global_coordinate import GlobalCoordinate


class SourceDestinationDto:

    def __init__(self, source_coordinate: GlobalCoordinate, destination_coordinate: GlobalCoordinate, source: str, destination: str):
        self.__source_coordinate = source_coordinate
        self.__destination_coordinate = destination_coordinate
        self.__source = source
        self.__destination = destination

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_source_coordinate(self):
        return self.__source_coordinate

    def get_destination_coordinate(self):
        return self.__destination_coordinate


