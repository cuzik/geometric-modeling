import os
import numpy as np
import scipy.special
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE


class Curve(object):
    """docstring for Curve"""

    def __init__(self, color_points, color_curve, screen, number_points, weigth=[1, 1, 1, 1, 1]):
        super(Curve, self).__init__()
        self.color_points = color_points
        self.color_curve = color_curve
        self.screen = screen
        self.step = 0.001
        self.weigth = weigth
        self.define_points_done = False
        self.number_points = number_points
        self.curve_points = []
        self.control_points = []
        self.define_control_points()
        self.define_curve_ponits()
        self.draw_all_struct()

    def define_curve_ponits(self):
        self.curve_points = []

    def draw_points(self):
        for point in self.control_points:
            pygame.draw.circle(self.screen, self.color_points, point, 4)

    def draw_edge(self):
        for i in range(0, len(self.control_points) - 1):
            pygame.draw.lines(
                self.screen,
                self.color_points,
                False,
                [self.control_points[i], self.control_points[i + 1]],
                1,
            )

    def draw_curve(self):
        pygame.draw.lines(self.screen, self.color_curve, False, self.curve_points, 1)
        # for curve_point in self.curve_points:
            # pygame.draw.circle(self.screen, self.color_curve, curve_point, 1)

    def draw_all_struct(self):
        self.draw_points()
        self.draw_edge()
        self.draw_curve()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.control_points += [pygame.mouse.get_pos()]
                if len(self.control_points) == self.number_points:
                    self.define_points_done = True
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.define_points_done = True

    def define_control_points(self):
        while not self.define_points_done:
            self.get_events()
            self.draw_points()
            self.draw_edge()
            pygame.display.flip()

        data = []
        for i in range(0, len(self.control_points)):
            for j in range(0, self.weigth[i]):
                data += [self.control_points[i]]

        self.old = self.control_points
        self.control_points = data

    def move(self, reference_point):
        diference_point = (
            self.control_points[0][0] - reference_point[0],
            self.control_points[0][1] - reference_point[1],
        )
        for i in range(0, len(self.control_points)):
            self.control_points[i] = (
                self.control_points[i][0] - diference_point[0],
                self.control_points[i][1] - diference_point[1],
            )
        self.define_curve_ponits()

    def last_control_point(self):
        return self.control_points[-1]

    def get_coefficient(self):
        p1 = self.control_points[0]
        p2 = self.control_points[1]

        index = 2

        while p2 == p1:
            p2 = self.control_points[index]
            index += 1

        if p2[0] - p1[0] == 0:
            return 1
        return (p2[1] - p1[1]) / float(p2[0] - p1[0])

    def change_penultimate_control_point(self, coefficient, alterator, x):
        self.control_points[-2] = (
            x + alterator,
            int(
                self.control_points[-1][1]
                + (x + alterator - self.control_points[-1][0]) * coefficient
            ),
        )
        self.define_curve_ponits()

    def calculate_function_par_last_points(self):
        print(self.curve_points[-10:])

    def calculate_function_par_first_points(self):
        print(self.curve_points[:10])
