# https://www.codewars.com/kata/5870fa11aa0428da750000da/train/python

import enum
import re
from typing import List
from typing import Tuple


@enum.unique
class Direction(enum.Enum):
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()


def execute(code: str) -> str:
    tokens: List[List[str, int]] = []
    for match_num, match in enumerate(re.finditer(r'([LFR])(\d*)', code, re.MULTILINE), start=1):
        token = []
        for group_num in range(0, len(match.groups())):
            token.append(match.group(group_num + 1))
        tokens.append(token)
    tokens: List[Tuple[str, int]] = [(t, 1 if c == '' else int(c)) for t, c in tokens]

    area: List[List[str]] = [['*']]
    direction = Direction.RIGHT
    traces = {(0, 0), }
    x, y = 0, 0
    for token, times in tokens:
        if token == 'L':
            for _ in range(times):
                direction = {
                    Direction.UP:    Direction.LEFT,
                    Direction.LEFT:  Direction.DOWN,
                    Direction.DOWN:  Direction.RIGHT,
                    Direction.RIGHT: Direction.UP,

                }.get(direction)
        elif token == 'R':
            for _ in range(times):
                direction = {
                    Direction.UP:    Direction.RIGHT,
                    Direction.RIGHT: Direction.DOWN,
                    Direction.DOWN:  Direction.LEFT,
                    Direction.LEFT:  Direction.UP,
                }.get(direction)
        elif token == 'F':
            for _ in range(times):
                x, y = {
                    Direction.UP:    lambda _x, _y: (_x + 0, _y + 1),
                    Direction.RIGHT: lambda _x, _y: (_x + 1, _y + 0),
                    Direction.DOWN:  lambda _x, _y: (_x + 0, _y - 1),
                    Direction.LEFT:  lambda _x, _y: (_x - 1, _y + 0),
                }.get(direction)(x, y)
                traces.add((x, y))
        else:
            raise Exception(token, times)

    min_x = min(x for x, _ in traces)
    max_x = max(x for x, _ in traces)
    min_y = min(y for _, y in traces)
    max_y = max(y for _, y in traces)
    area = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            if (x, y) in traces:
                row.append('*')
            else:
                row.append(' ')
        area.append(row)

    return '\r\n'.join([''.join(row) for row in reversed(area)])
