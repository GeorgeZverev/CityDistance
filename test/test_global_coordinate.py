from global_coordinate import GlobalCoordinate


def test_global_coordinate():
    coordinate = GlobalCoordinate(55.7558, 37.6172)
    assert coordinate is not None


def test_get_latitude_longitude():
    coordinate = GlobalCoordinate(55.7558, 37.6172)
    assert coordinate.get_latitude() == 55.7558

    assert coordinate.get_longitude() == 37.6172