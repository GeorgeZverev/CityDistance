import math
from my_error import MyError


class DistanceCalculator:

    def __init__(self):
        self.__city_one = ()
        self.__city_two = ()

    def calculate_distance(self, city_one: (), city_two: ()) -> float:
        if self.__validate(city_one[0]) is False or self.__validate(city_one[1]) is False or self.__validate(city_two[0]) is False or self.__validate(city_two[1]) is False:
            return 0
        if self.__validate_tuple(city_one) is False or self.__validate_tuple(city_two) is False:
            return 0
        self.__city_one, self.__city_two = self.__radian_calculate(city_one, city_two)
        circumference_earth = 6371
        cos_d = math.sin(self.__city_one[0]) * math.sin(self.__city_two[0]) + math.cos(self.__city_one[0]) * math.cos(self.__city_two[0]) * math.cos(
            self.__city_one[1] - self.__city_two[1])
        d = math.acos(cos_d)
        length = d * circumference_earth
        length = round(length, 1)
        return length

    def __radian_calculate(self, city_one_param: (), city_two_param: ()) -> ():
        self.__city_one = city_one_param
        self.__city_two = city_two_param
        city_one = []
        city_two = []
        for element in self.__city_one:
            if type(element) is str:
                raise MyError('elements must be float')
            res_one = element * (math.pi / 180)
            city_one.append(round(res_one, 4))
        for element in self.__city_two:
            res_two = element * (math.pi / 180)
            city_two.append(round(res_two, 4))
        city_one = tuple(city_one)
        city_two = tuple(city_two)
        return city_one, city_two

    @staticmethod
    def __validate(city: float) -> bool:
        return -180 <= city <= 180

    @staticmethod
    def __validate_tuple(city: ()) -> bool:
        return city != (0, 0)


