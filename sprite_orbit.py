#!/usr/bin/env python3
"""sprite_orbit.py: particles orbit around a graphic
© 2021 JonLiuFYI, licensed GPL v3.
"""
from dataclasses import dataclass

import pyxel as px


WIDTH = 128
HEIGHT = 128


class SpriteOrbit:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)

        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(0)


SpriteOrbit()
