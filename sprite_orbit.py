#!/usr/bin/env python3
"""sprite_orbit.py: particles orbit around a graphic
© 2021 JonLiuFYI, licensed GPL v3.
"""
from dataclasses import dataclass
from math import cos, sin, pi

import pyxel as px


WIDTH = 128
HEIGHT = 128


class SpriteOrbit:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)
        px.load("assets/demo-fx.pyxres")

        self.sprites = [Sprite(x * 0.25 * pi, over=(not 2 <= x <= 5)) for x in range(8)]
        self.logostrips = [LogoStrip(n) for n in range(0, 38)]

        px.run(self.update, self.draw)

    def update(self):
        [s.update() for s in self.sprites]
        [strip.update() for strip in self.logostrips]

    def draw(self):
        px.cls(0)

        [s.draw() for s in self.sprites if not s.over]
        [strip.draw() for strip in self.logostrips]
        [s.draw() for s in self.sprites if s.over]


@dataclass
class Sprite:
    # centre (x,y) will be (3,3) in the sprite
    delay: int  # radians
    x: int = 0
    y: int = 0

    # True/False determined by delay angle at init time
    over: bool = True

    def update(self):
        fc = px.frame_count
        yscale = 30 + 14 * sin(fc / 50)
        self.y = yscale * sin(fc / 25 + self.delay) + 64
        # self.x = 20 * cos(fc / 25 + self.delay) + 64
        self.x = 30 * cos(fc / 15 + self.delay) + 64

        # going down is under
        if self.y <= (66 - yscale) and self.over:
            self.over = False

        # going up is over
        if self.y >= (62 + yscale) and not self.over:
            self.over = True

        # print("OVER" if self.over else "under")

    def draw(self):
        px.blt(self.x - 3, self.y - 3, 0, 8 * self.over, 32, 8, 8, 14)


class LogoStrip:
    def __init__(self, stripnum):
        self.stripnum = stripnum
        self.x = 26 + 2 * stripnum
        self.y = 48

    def update(self):
        self.y = 6 * sin(px.frame_count / 20 + self.stripnum / 12) + 48

    def draw(self):
        px.blt(self.x, self.y, 0,
                2 * self.stripnum, 0,
                2, 32,
                0)


SpriteOrbit()
