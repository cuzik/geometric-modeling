import os
import numpy as np
import scipy.special
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE

class Curve(object):
  """docstring for Curve"""
  def __init__(self, color_points, color_curve, screen):
    super(Curve, self).__init__()
    self.color_points = color_points
    self.color_curve = color_curve
    self.screen = screen
    self.define_points_done = False
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
    for i in range(0,len(self.control_points)-1):
      pygame.draw.lines(self.screen, self.color_points, False , [self.control_points[i], self.control_points[i+1]], 1)

  def draw_curve(self):
    # pygame.draw.lines(self.screen, self.color_curve, False, self.curve_points, 3)
    for point in self.curve_points:
      pygame.draw.circle(self.screen, self.color_curve, (int(point[0]),int(point[1])), 1)

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
      elif event.type == KEYDOWN and event.key == K_SPACE:
        self.define_points_done = True

  def define_control_points(self):
    while not self.define_points_done:
      self.get_events()
      self.draw_points()
      self.draw_edge()
      pygame.display.flip()

  def move(self, reference_point):
    diference_point = (self.control_points[0][0] - reference_point[0], self.control_points[0][1] - reference_point[1])
    for i in range(0,len(self.control_points)):
      self.control_points[i] = (self.control_points[i][0] - diference_point[0], self.control_points[i][1] - diference_point[1])
    self.define_curve_ponits()

  def last_control_point(self):
    return self.control_points[-1]

  def get_coefficient(self):
    if self.control_points[1][0] - self.control_points[0][0] == 0:
      return 1
    return (self.control_points[1][1] - self.control_points[0][1]) / float  (self.control_points[1][0] - self.control_points[0][0])

  def change_penultimate_control_point(self, coefficient):
    self.control_points[-2] = (self.control_points[-2][0], int(self.control_points[-1][1] + (self.control_points[-2][0] - self.control_points[-1][0]) * coefficient))
    self.define_curve_ponits()

  def aa(self):
    self.control_points[-2] = (self.control_points[-1][0] * 2 - self.control_points[-2][0], self.control_points[-1][1] * 2 - self.control_points[-2][1])
    self.define_curve_ponits()
