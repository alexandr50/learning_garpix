class Cuboid:

    def __init__(self, lenght, width, height):
        self.lenght = lenght
        self.width = width
        self.height = height

    def calculate_v(self):
        return self.width * self.lenght * self.height

    def calculate_floor_space(self):
        return self.width * self.lenght

    def calculate_side_s(self):
        return self.width * self.height

    @staticmethod
    def info():
        print(f'''Расчет обьема фигуры: calculate_v,
Расчет площади основания: calculate_floor_space,
Расчет площади боковой стороны: calculate_side_s''')

c = Cuboid(2, 3, 4)
print(c.calculate_v())
print(c.calculate_floor_space())
print(c.calculate_side_s())
c.info()