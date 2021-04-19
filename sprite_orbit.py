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

        self.sprites = [Sprite(x * 0.25 * pi) for x in range(8)]

        px.run(self.update, self.draw)

    def update(self):
        [s.update() for s in self.sprites]

    def draw(self):
        px.cls(0)

        [s.draw() for s in self.sprites if not s.over]
        px.blt(26, 48, 0, 0, 0, 76, 32, 0)
        [s.draw() for s in self.sprites if s.over]


@dataclass
class Sprite:
    # centre (x,y) will be (3,3) in the sprite
    delay: int
    x: int = 0
    y: int = 0

    over: bool = True
    # TODO: programatically determine True/False based on vertical direction

    def update(self):
        fc = px.frame_count
        self.y = 30 * sin(fc / 25 + self.delay) + 64
        # self.x = 20 * cos(fc / 25 + self.delay) + 64
        self.x = 30 * cos(fc / 15 + self.delay) + 64

        # going down is under
        if self.y <= 35 and self.over:
            self.over = False

        # going up is over
        if self.y >= 93 and not self.over:
            self.over = True

        # print("OVER" if self.over else "under")

    def draw(self):
        px.blt(self.x - 3, self.y - 3, 0, 0, 32, 8, 8, 14)


SpriteOrbit()
