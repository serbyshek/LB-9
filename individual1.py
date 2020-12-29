#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# . Создать класс Angle для работы с углами на плоскости, задаваемыми величиной в градусах
# и минутах. Обязательно должны быть реализованы: перевод в радианы, приведение к
# диапазону 0-360, увеличение и уменьшение угла на заданную величину, получение синуса,
# сравнение углов.

import math

class Angle:

    def __init__(self):

        self.__a = 0
        self.__b = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(';')))

        for part in parts:
            if part == 0:
                raise ValueError()

            self.__a = float(parts[0])
            self.__b = float(parts[1])
            self.range()

    def range(self):
        if self.__a < 0:
            self.__a = 360 - self.__a
        elif self.__b < 0:
            self.__b = 360 - self.__b
        elif self.__a > 360:
            self.__a = self.__a - 360
        elif self.__b > 360:
            self.__b = self.__b - 360

    def change(self, a,b):
        self.__a = a
        self.__b = b

    def rad(self):
        return math.radians(self.__a), math.radians(self.__b)

    def sin(self):
        return math.sin(self.__a), math.sin(self.__b)

    def eq(self):
        if self.__a == self.__b:
            return True
        else:
            return False

    def dispaly(self):
        print("Искомые величины: "
              "Перевод в радианы: {}; "
              "sin={}; "
              "Сравнение углов {} "
              .format(self.rad(), self.sin(), self.eq())
              )
if __name__ == '__main__':
    C = Angle()
    C.read("Введите два угла через ;")
    C.dispaly()

    # # Изменение сторон и их получение
    print(C.change(10, 140))
    C.dispaly()