#!/usr/bin/env python3
"""simple_scroll.py: a wavy text scroller
© 2021 JonLiuFYI, licensed GPL v3.
"""
from math import sin

import pyxel as px


class SimpleScroll:
    def __init__(self) -> None:
        px.init(256, 256, fps=60)

        self.x = px.width + 5
        self.y = 128

        self.msg = [
            Letter(c, self.x + 5 * i, self.y)
            for i, c in enumerate("I liek chocolate milk!")
        ]

        px.run(self.update, self.draw)

    def update(self) -> None:
        for l in self.msg:
            l.update()

    def draw(self) -> None:
        px.cls(0)
        for l in self.msg:
            l.draw()


class Letter:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y

    def update(self):
        self.x = (self.x - 1) % (px.width + 5)
        self.y = 128 + 30 * sin(px.frame_count / 20 - self.x / 70)

    def draw(self):
        px.text(self.x, self.y, self.letter, 8)


SimpleScroll()
