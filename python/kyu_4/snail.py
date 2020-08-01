# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

from typing import List


def snail(snail_map: List[List[int]]) -> List[int]:
    bound_x_lower: int = 0
    bound_x_upper: int = len(snail_map[0])
    bound_y_lower: int = 0
    bound_y_upper: int = len(snail_map)
    result = []
    while bound_x_lower < bound_x_upper and bound_y_lower < bound_y_upper:
        for x in range(bound_y_lower, bound_y_upper):
            result.append(snail_map[bound_x_lower][x])
        bound_x_lower += 1

        for y in range(bound_x_lower, bound_x_upper):
            result.append(snail_map[y][bound_y_upper - 1])
        bound_y_upper -= 1

        if bound_x_lower < bound_x_upper:
            for x in range(bound_y_upper - 1, bound_y_lower - 1, -1):
                result.append(snail_map[bound_x_upper - 1][x])
            bound_x_upper -= 1

        if bound_y_lower < bound_y_upper:
            for y in range(bound_x_upper - 1, bound_x_lower - 1, -1):
                result.append(snail_map[y][bound_y_lower])
            bound_y_lower += 1

    return result
