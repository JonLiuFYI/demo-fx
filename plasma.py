#!/usr/bin/env python3
"""plasma.py: an attempt at a plasma effect
© 2021 JonLiuFYI, licensed GPL v3.
"""
from math import sin, cos, sqrt
from typing import List

import pyxel as px


class Plasma:
    def __init__(self):
        px.init(64, 64, fps=60)

        # self.cols = [0, 1, 5, 12, 6, 7]
        self.cols = [15, 14, 8, 2, 4, 9, 10, 11, 3, 1, 5, 12, 6, 7]

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)

        for y in range(px.height):
            for x in range(px.width):
                # simple stripes
                # this_colour = 2.2 * sin(x / 6 + px.frame_count / 20) + 2.5

                # spinning stripes
                # this_colour = (
                #     2.2
                #     * sin(
                #         (x * sin(px.frame_count / 27) + y * cos(px.frame_count / 21))
                #         / 4
                #         + px.frame_count / 20
                #     )
                #     + 2.5
                # )

                # complicated
                # this_colour = (
                #     2.2
                #     * sin(
                #         (x * sin(px.frame_count / 27) + y * cos(px.frame_count / 21))
                #         / 4
                #         + sin(x / 6 + px.frame_count / 30) / 2
                #         + cos(y / 1.6 + px.frame_count / 50)
                #         + px.frame_count / 20
                #     )
                #     + 2.5
                # )

                # circle
                cx = x + 28 * sin(px.frame_count / 50) - px.width / 2
                cy = y + 19 * cos(px.frame_count / 30) - px.height / 2
                # this_colour = (
                #     2.2
                #     * sin(sqrt((cx ** 2 + cy ** 2) / 5 + 1000) + px.frame_count / 15)
                #     + 2.5
                # )

                # composite
                this_colour = (
                    3.1
                    * (
                        sin(
                            (
                                x * sin(px.frame_count / 27)
                                + y * cos(px.frame_count / 21)
                            )
                            / 9
                            # + sin(x / 6 + px.frame_count / 30) / 2
                            # + cos(y / 1.6 + px.frame_count / 50)
                            + px.frame_count / 20
                        )
                        + sin(
                            sqrt((cx ** 2 + cy ** 2) / 5 + 1000) + px.frame_count / 15
                        )
                    )
                    + 6.5
                )

                px.pset(x, y, self.cols[round(this_colour)])


Plasma()
