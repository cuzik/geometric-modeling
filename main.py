import os
import numpy as np
import scipy.special
import pygame
from pygame.locals import *

from curve import Curve
from bezier import Bezier
from nurbs import Nurbs

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption('Modelagem Geometrica TOP')
screen.fill((22, 22, 22))

game_run = True
only_curve = False

bezier_curve = Bezier([150, 0, 0], [200, 200, 0], screen)
nurbs_curve  = Nurbs([0, 150, 0], [0, 200, 200], screen)

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
      bezier_curve.change_penultimate_control_point(nurbs_curve.get_coefficient())
    elif event.type == KEYDOWN and event.key == K_a:
      bezier_curve.aa()
    elif event.type == KEYDOWN and event.key == K_c:
      only_curve = only_curve == False

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

if __name__ == '__main__':
  main()
