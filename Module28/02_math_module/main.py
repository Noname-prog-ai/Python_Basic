# TODO здесь писать код
class mymath:
    @staticmethod
    def circle_len(radius: float) -> float:
        """
        Вычисляет длину окружности

        :param radius: Радиус окружности
        :return: Длина окружности
        """
        return 2 * 3.141592653589793 * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        """
        Вычисляет площадь окружности

        :param radius: Радиус окружности
        :return: Площадь окружности
        """
        return 3.141592653589793 * radius ** 2

    @staticmethod
    def cube_vol(side_length: float) -> float:
        """
        Вычисляет объём куба

        :param side_length: Длина стороны куба
        :return: Объём куба
        """
        return side_length ** 3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        """
        Вычисляет площадь поверхности сферы

        :param radius: Радиус сферы
        :return: Площадь поверхности сферы
        """
        return 4 * 3.141592653589793 * radius ** 2


res_1 = mymath.circle_len(radius=5)
res_2 = mymath.circle_sq(radius=6)
print(res_1)  # Вывод: 31.41592653589793
print(res_2)  # Вывод: 113.09733552923255