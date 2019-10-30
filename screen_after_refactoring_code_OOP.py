#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

"""
Реализовать класс 2-мерных векторов Vec2d [1]. В классе следует определить методы для основных математических операций, 
необходимых для работы с вектором: Vec2d.__add__ (сумма), Vec2d.__sub__ (разность), Vec2d.__mul__ (произведение на число). 
А также добавить возможность вычислять длину вектора с использованием функции len(a) и метод int_pair, который возвращает 
кортеж из двух целых чисел (текущие координаты вектора).
"""

class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __len__(self) :
        """возвращает длину вектора"""
        return math.sqrt(self.x**2 + self.y**2)

    def __mul__(self, other):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * other, self.y * other)

    def int_pair(self):
        """возвращает кортеж из двух целых чисел (текущие координаты вектора)"""
        return self.x, self.y

"""
Реализовать класс замкнутых ломаных Polyline с методами отвечающими за добавление в ломаную точки (Vec2d) c её 
скоростью, пересчёт координат точек (set_points) и отрисовку ломаной (draw_points). Арифметические действия с векторами 
должны быть реализованы с помощью операторов, а не через вызовы соответствующих методов.
"""

class Polyline:
    def __init__(self, surface, color):
        self.surface = surface # gameDisplay = pygame.display.set_mode(SCREEN_DIM)
        self.points = []  # [[point, speed_point], ]
        self.color_line = color # pygame.Color(0)
        self.color_point = (255, 255, 255)
        self.width=3

        self.count = 0

    def _gen_color(self):
        self.count += 1
        hue = (self.count + 1) % 360
        self.color_line.hsla = (hue, 100, 50, 100)

    def add_point(self, point, point_speed):
        self.points.append([point, point_speed])

    def draw_points(self, style="points"):
        """функция отрисовки точек на экране"""

        self._gen_color()

        if style == "line" and len(self.points) > 3:
            for p_n in range(-1, len(self.points) - 1):
                print(self.points[p_n])
                pygame.draw.line(self.surface, self.color_line,
                                 (int(self.points[p_n][0].x), int(self.points[p_n][0].y)),
                                 (int(self.points[p_n + 1][0].x), int(self.points[p_n + 1][0].y)), self.width)

        elif style == "points":
            for p, _ in self.points:
                pygame.draw.circle(self.surface, self.color_point,
                                   (int(p.x), int(p.y)), self.width)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for point, point_speed in self.points:
            point.x = point.x + point_speed.x
            point.y = point.y + point_speed.y
            if point.x > SCREEN_DIM[0] or point.x < 0:
                point_speed.x = -point_speed.x
            if point.y > SCREEN_DIM[1] or point.y < 0:
                point_speed.y = -point_speed.y


"""
Реализовать класс Knot (наследник класса Polyline), в котором добавление и пересчёт координат инициируют вызов 
функции get_knot для расчёта точек кривой по добавляемым «опорным» точкам [2].
"""

class Knot(Polyline):
    def __init__(self, surface, color, step=35):
        super(Knot, self).__init__(surface, color)
        self.step = step # need changed

    def set_step_up(self):
        self.step += 1

    def set_step_down(self):
        self.step -= 1 if self.step > 1 else 0

    def _get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]

        return points[deg] * alpha + self._get_point(points, alpha, deg - 1) * (1 - alpha)

    def _get_points(self, base_points):
        alpha = 1 / self.step
        res = []
        for i in range(self.step):
            res.append(self._get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        res = []
        if len(self.points) > 3:
            for i in range(-2, len(self.points) - 2):
                ptn = []
                ptn.append((self.points[i][0] + self.points[i + 1][0]) * 0.5)
                ptn.append(self.points[i + 1][0])
                ptn.append((self.points[i + 1][0] + self.points[i + 2][0]) * 0.5)

                res.extend(self._get_points(ptn))
        self.draw_points()
        self.draw_points(style="line", points=res)

    def draw_points(self, style="points", points=None):
        """функция отрисовки точек на экране"""

        self._gen_color()

        if style == "line" and points:
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(self.surface, self.color_line,
                                 (int(points[p_n].x), int(points[p_n].y)),
                                 (int(points[p_n + 1].x), int(points[p_n + 1].y)), self.width)

        elif style == "points":
            for p, _ in self.points:
                pygame.draw.circle(self.surface, self.color_point,
                                   (int(p.x), int(p.y)), self.width)


def start_screen():
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    working = True
    show_help = False
    pause = True
    color = pygame.Color(0)
    polyline = Knot(gameDisplay, color)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Knot(gameDisplay, color)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    polyline.set_step_up()
                if event.key == pygame.K_KP_MINUS:
                    polyline.set_step_down()
                # if event.key == pygame.K_F1:
                #     show_help = not show_help

            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.add_point(Vec2d(*event.pos), Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        # polyline.draw_points()
        # polyline.draw_points(style="line")
        polyline.get_knot()
        if not pause:
            polyline.set_points()
        # if show_help:
        #     draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)

if __name__ == "__main__":
    start_screen()