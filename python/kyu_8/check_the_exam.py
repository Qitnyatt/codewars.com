# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

from typing import List


def check_exam(arr1: List[int], arr2: List[int]) -> int:
    result: int = 0
    for i in range(len(arr1)):
        if arr2[i] == '':
            continue
        if arr1[i] != arr2[i]:
            result += -1
        if arr1[i] == arr2[i]:
            result += 4
    return 0 if result < 0 else result
