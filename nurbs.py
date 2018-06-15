import numpy as np
import scipy.special
from curve import Curve


class Nurbs(Curve):
    """docstring for Nerbs"""

    def define_curve_ponits(self):
        self.curve_points = []
        n = len(self.control_points) - 1
        for t in np.arange(0, 1.0 + self.step, self.step):
            b_point_x = 0
            b_point_y = 0
            for i in range(0, len(self.control_points)):
                binomial_coefficient = scipy.special.binom(n, i)
                b_point_x += (
                    ((1 - float(t)) ** (n - i))
                    * (t ** i)
                    * self.control_points[i][0]
                    * binomial_coefficient
                )
                b_point_y += (
                    ((1 - float(t)) ** (n - i))
                    * (t ** i)
                    * self.control_points[i][1]
                    * binomial_coefficient
                )
            self.curve_points += [(int(b_point_x), int(b_point_y))]
