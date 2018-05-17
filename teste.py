import os
import numpy as np
import scipy.special
import pygame
from pygame.locals import *

structs = {
           'first' : {
                        'number_points': 4,
                        'points': [],
                          'color_points': [216, 67, 21],
                        'color_curve': [255,255,0],
                        'curve_points': []
                     },
           'second': {
                        'number_points': 4,
                        'points': [],
                        'color_points': [26, 35, 126],
                        'color_curve': [0,255,0],
                        'curve_points': []
                      }
         }

heigth = 700
width = 1200

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Modelagem geometrica')
screen.fill((20, 20, 20))

game_run = True
define_points_done = False

def define_bezier(points):
  n = len(points) - 1
  bezier_points = []
  for t in np.arange(0, 1.0, 0.0001):
    b_point_x = 0
    b_point_y = 0
    for i in range(0, len(points)):
      binomial_coefficient = scipy.special.binom(n, i)
      b_point_x += ((1-float(t))**(n-i))*(t**i)*points[i][0] * binomial_coefficient
      b_point_y += ((1-float(t))**(n-i))*(t**i)*points[i][1] * binomial_coefficient
    bezier_points += [(b_point_x, b_point_y)]
  return bezier_points

def draw_points(color, points):
  for point in points:
    pygame.draw.circle(screen, color, point, 4)

def draw_curve(color, points):
  pygame.draw.lines(screen, color, False, points, 2)

def draw_edge(color, points):
  for i in range(0,len(points)-1):
    pygame.draw.lines(screen, color,False , [points[i], points[i+1]], 1)

def move_c0():
  global structs
  diference_point = (structs['second']['points'][0][0] - structs['first']['points'][-1][0], structs['second']['points'][0][1] - structs['first']['points'][-1][1])
  for i in range(0,len(structs['second']['points'])):
    structs['second']['points'][i] = (structs['second']['points'][i][0] - diference_point[0], structs['second']['points'][i][1] - diference_point[1])
  structs['second']['curve_points'] = define_bezier(structs['second']['points'])
  draw_all_structs()

def draw_all_structs():
  screen.fill((20,  20, 20))
  for key, value in structs.items():
    draw_points(structs[key]['color_points'], structs[key]['points'])
    draw_edge(structs[key]['color_points'], structs[key]['points'])
    draw_curve(structs[key]['color_curve'], structs[key]['curve_points'])
  pygame.display.flip()

def get_events_draw():
  global game_run
  for event in pygame.event.get():
    if event.type == QUIT:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_SPACE:
      move_c0()

def get_events_points(label):
  global structs
  global game_run
  global define_points_done
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      structs[label]['points'] += [pygame.mouse.get_pos()]
    elif event.type == QUIT:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      game_run = False
    elif event.type == KEYDOWN and event.key == K_SPACE:
      define_points_done = True

def define_points():
  global define_points_done
  for key in ['first', 'second']:
    define_points_done = False
    while game_run and not define_points_done:
      pygame.display.flip()
      get_events_points(key)
      draw_points(structs[key]['color_points'], structs[key]['points'])
    structs[key]['curve_points'] = define_bezier(structs[key]['points'])
    draw_points(structs[key]['color_points'], structs[key]['points'])
    draw_edge(structs[key]['color_points'], structs[key]['points'])
    draw_curve(structs[key]['color_curve'], structs[key]['curve_points'])




define_points()
while game_run:
  get_events_draw()
  draw_all_structs()
