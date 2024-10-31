
from global_coordinate import GlobalCoordinate
from source_destination_dto import SourceDestinationDto


def test_source_destination_dto():
    source_coordinate = GlobalCoordinate(35.6897, 139.6922)
    destination_coordinate = GlobalCoordinate(34.6939, 135.5022)
    instance = SourceDestinationDto(source_coordinate, destination_coordinate, 'Japan,Tokyo', 'Japan,Osaka')
    assert instance is not None

    assert instance.get_source_coordinate().get_latitude() == 35.6897
    assert instance.get_source_coordinate().get_longitude() == 139.6922

    assert instance.get_destination_coordinate().get_latitude() == 34.6939
    assert instance.get_destination_coordinate().get_longitude() == 135.5022

    assert instance.get_source() == 'Japan,Tokyo'

    assert instance.get_destination() == 'Japan,Osaka'
