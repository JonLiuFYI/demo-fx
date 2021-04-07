#!/usr/bin/env python3
"""chasm.py: pseudo-3D effect of flying over a deep chasm
© 2021 JonLiuFYI, licensed GPL v3.
"""

import pyxel as px


WIDTH = 128
HEIGHT = 128


class Chasm:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)

        self.gradient = [6, 12, 5, 1, 0, 0, 1, 5, 12, 6]

        self.gradient_w = 3
        self.gradient_offset = (
            WIDTH // 2 - self.gradient_w * (len(self.gradient) // 2) + 1
        )

        self.strip_w = 45
        self.strip_h = HEIGHT // 4
        self.strips = [
            # left
            Strip(0, HEIGHT - self.strip_h, self.strip_w, self.strip_h),
            Strip(0, HEIGHT - 3 * self.strip_h, self.strip_w, self.strip_h),
            Strip(0, HEIGHT - 5 * self.strip_h, self.strip_w, self.strip_h),
            # right
            Strip(
                WIDTH - self.strip_w, HEIGHT - self.strip_h, self.strip_w, self.strip_h
            ),
            Strip(
                WIDTH - self.strip_w,
                HEIGHT - 3 * self.strip_h,
                self.strip_w,
                self.strip_h,
            ),
            Strip(
                WIDTH - self.strip_w,
                HEIGHT - 5 * self.strip_h,
                self.strip_w,
                self.strip_h,
            ),
        ]

        px.run(self.update, self.draw)

    def update(self):
        [s.update() for s in self.strips]

    def draw(self):
        fc = px.frame_count
        px.cls(7)

        for i, c in enumerate(self.gradient):
            px.rect(
                i * self.gradient_w + self.gradient_offset,
                0,
                self.gradient_w,
                HEIGHT,
                c,
            )

        [s.draw() for s in self.strips]

        # FIXME: centre for reference
        px.pset(WIDTH // 2, HEIGHT // 2, 8)


class Strip:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
        self.y -= 1
        if self.y < -2 * self.h:
            self.y = HEIGHT

    def draw(self):
        px.rect(self.x, self.y, self.w, self.h, 0)


Chasm()
