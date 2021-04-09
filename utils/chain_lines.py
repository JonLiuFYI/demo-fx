#!/usr/bin/env python3
"""chain_lines.py: Generate Pyxel line() calls from one given point to the next.
© 2021 JonLiuFYI, licensed GPL v3.

Usage:
From your present working directory, create a plain text file called `coords`.
Still in your pwd, run this.

`coords`has this format, where X and Y values are relative to an origin that's
in the top left:
    X1 Y1
    X2 Y2
    X3 Y3
    ...

Customize the print string as needed, such as the colour or the arithmetic
around the coordinate values.

In the current print string:
* (CX, CY) is the origin that the lines are drawn relative to. Define it in
    whatever script you paste this output to
* s is a scaling modifier that changes over time
"""

with open("coords", "r") as coords:
    prev_x = None
    prev_y = None
    for point in coords:
        x, y = point.split()

        if prev_x is None:
            prev_x, prev_y = x, y
            continue

        print(f"px.line(CX+{x}*s, CY+{y}*s, CX+{prev_x}*s, CY+{prev_y}*s, 9)")
        prev_x, prev_y = x, y
