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
screen.fill((20, 20, 20))

game_run = True

bezier_curve = Bezier([216, 67, 21], [255,255,0], screen)
nurbs_curve  = Nurbs([26, 35, 126], [0,255,0], screen)

def get_events_draw():
  global game_run
  for event in pygame.event.get():
    if event.type == QUIT:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_SPACE:
      nurbs_curve.move(bezier_curve.last_control_point())

def main():
  while game_run:
    get_events_draw()
    screen.fill((20,  20, 20))
    bezier_curve.draw_all_struct()
    nurbs_curve.draw_all_struct()
    pygame.display.flip()

if __name__ == '__main__':
  main()
