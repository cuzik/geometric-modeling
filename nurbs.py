import numpy as np
import scipy.special
from curve import Curve


class Nurbs(Curve):
    """docstring for Nurbs"""

    def parcer_N(self, t):
        n = len(self.control_points) - 1
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
        return (b_point_x, b_point_y)

    def define_curve_ponits(self):
        self.curve_points = []
        for t in np.arange(0, 1.0 + self.step, self.step):
            b_point_x, b_point_y = self.parcer_N(t)
            self.curve_points += [(int(b_point_x), int(b_point_y))]

    def first_derivate(self):
        return (
            (
                -3 * self.old[0][0] * (1 - 0) ** 2
                + 3 * self.old[1][0] * (1 - 0) ** 2
                - 6 * self.old[1][0] * (1 - 0) * 0
                + 6 * self.old[2][0] * (1 - 0) * 0
                - 3 * self.old[2][0] * 0 ** 2
                + 3 * self.old[3][0] * 0 ** 2
            ),
            (
                -3 * self.old[0][1] * (1 - 0) ** 2
                + 3 * self.old[1][1] * (1 - 0) ** 2
                - 6 * self.old[1][1] * (1 - 0) * 0
                + 6 * self.old[2][1] * (1 - 0) * 0
                - 3 * self.old[2][1] * 0 ** 2
                + 3 * self.old[3][1] * 0 ** 2
            ),
        )

    def second_derivate(self):
        return (
            (
                -6
                * (
                    -self.old[2][0]
                    + self.old[1][0] * (2 - 3 * 0)
                    - self.old[0][0] * (1 - 0)
                    + 3 * self.old[2][0] * 0
                    - self.old[3][0] * 0
                )
            ),
            (
                -6
                * (
                    -self.old[2][1]
                    + self.old[1][1] * (2 - 3 * 0)
                    - self.old[0][1] * (1 - 0)
                    + 3 * self.old[2][1] * 0
                    - self.old[3][1] * 0
                )
            ),
        )
