import os
import numpy as np
import scipy.special
import pygame
import time
import random
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_0, K_1, K_2, K_c

from bezier import Bezier
from nurbs import Nurbs

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("Modelagem Geometrica TOP")
screen.fill((22, 22, 22))

game_run = True
only_curve = False
erro = 1

bezier_curve = Bezier([150, 0, 0], [200, 200, 0], screen, 4)
nurbs_curve = Nurbs([0, 150, 0], [0, 200, 200], screen, 5, [2, 3, 4, 3, 2])


def get_events_draw():
    global game_run
    global only_curve
    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            game_run = False
        elif event.type == KEYDOWN and event.key == K_0:
            nurbs_curve.move(bezier_curve.last_control_point())
        elif event.type == KEYDOWN and event.key == K_1:
            print("WIP C1")
            define_c1()
            print("DONE C1")
        elif event.type == KEYDOWN and event.key == K_2:
            print("WIP C2")
            define_c2()
            print("DONE C2")
        elif event.type == KEYDOWN and event.key == K_c:
            only_curve = only_curve == False


def define_c1():
    increment = 1

    while not (
        abs(bezier_curve.first_derivate()[0] - nurbs_curve.first_derivate()[0]) < erro
    ):
        # print(bezier_curve.first_derivate(), nurbs_curve.first_derivate(), increment)

        bezier_curve.control_points[-2] = (
            bezier_curve.control_points[-2][0] + increment,
            bezier_curve.control_points[-2][1],
        )

        draw_full_screen()

        if (abs(bezier_curve.control_points[-2][0]) > 1000):
            increment = -increment

    increment = 1

    while not (
        abs(bezier_curve.first_derivate()[1] - nurbs_curve.first_derivate()[1]) < erro
    ):
        # print(bezier_curve.first_derivate(), nurbs_curve.first_derivate(), increment)

        bezier_curve.control_points[-2] = (
            bezier_curve.control_points[-2][0],
            bezier_curve.control_points[-2][1] + increment,
        )

        draw_full_screen()

        if (abs(bezier_curve.control_points[-2][1]) > 1000):
            increment = -increment


def define_c2():
    increment = 1

    while not (
        abs(bezier_curve.second_derivate()[0] - nurbs_curve.second_derivate()[0]) < erro
    ):
        # print(
        #     bezier_curve.second_derivate()[0] - nurbs_curve.second_derivate()[0],
        #     bezier_curve.second_derivate()[1] - nurbs_curve.second_derivate()[1],
        # )

        bezier_curve.control_points[-3] = (
            bezier_curve.control_points[-3][0] + increment,
            bezier_curve.control_points[-3][1],
        )
        bezier_curve.define_curve_ponits()

        draw_full_screen()

        if (
            abs(bezier_curve.control_points[-3][0]) > 1000
        ):
            increment = -increment

    increment = 1

    while not (
        abs(bezier_curve.second_derivate()[1] - nurbs_curve.second_derivate()[1]) < erro
    ):
        # print(
        #     bezier_curve.second_derivate()[0] -
        #     nurbs_curve.second_derivate()[0],
        #     bezier_curve.second_derivate()[1] -
        #     nurbs_curve.second_derivate()[1],
        # )

        bezier_curve.control_points[-3] = (
            bezier_curve.control_points[-3][0],
            bezier_curve.control_points[-3][1] + increment,
        )
        bezier_curve.define_curve_ponits()

        draw_full_screen()

        if (
            abs(bezier_curve.control_points[-3][1]) > 1000
        ):
            increment = -increment

    print(
        bezier_curve.second_derivate()[0] - nurbs_curve.second_derivate()[0],
        bezier_curve.second_derivate()[1] - nurbs_curve.second_derivate()[1],
    )

def draw_full_screen():
    bezier_curve.define_curve_ponits()
    screen.fill((22, 22, 22))
    bezier_curve.draw_all_struct()
    nurbs_curve.draw_all_struct()
    pygame.display.flip()


def main():
    while game_run:
        get_events_draw()
        screen.fill((22, 22, 22))
        if only_curve:
            bezier_curve.draw_curve()
            nurbs_curve.draw_curve()
        else:
            bezier_curve.draw_all_struct()
            nurbs_curve.draw_all_struct()
        pygame.display.flip()


if __name__ == "__main__":
    main()
