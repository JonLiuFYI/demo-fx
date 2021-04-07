#!/usr/bin/env python3
"""plasma.py: an attempt at a plasma effect
© 2021 JonLiuFYI, licensed GPL v3.
"""
from math import sin, cos, sqrt

import pyxel as px


WIDTH = 64
HEIGHT = 64


class Plasma:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)

        self.colours = [15, 14, 8, 2, 4, 9, 10, 11, 3, 1, 5, 12, 6, 7]

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        fc = px.frame_count

        for y in range(HEIGHT):
            for x in range(WIDTH):
                # circle centre
                circx = x + 28 * sin(fc / 50) - WIDTH / 2
                circy = y + 19 * cos(fc / 30) - HEIGHT / 2

                # ideal amplitude is 6.2, a bit less than half of len(colours)-1,
                #   so the wave reaches much of the palette range
                # ideal height is +6.5, half of len(colours)-1, to put the wave's
                #   axis in the middle of the palette
                this_colour = round(
                    # (ideal amplitude / number of inner functions), eg. 6.2 / 2 = 3.1
                    3.1
                    * (
                        sin((x * sin(fc / 27) + y * cos(fc / 21)) / 9 + fc / 20)
                        + sin(
                            sqrt((circx * circx + circy * circy) / 5 + 1000) + fc / 15
                        )
                    )
                    + 6.5
                )

                px.pset(x, y, self.colours[this_colour])


Plasma()
