# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python


def int32_to_ip(int32):
    return '.'.join(
        f'{(int32 & x) >> y}' for x, y in (
            (0xff_00_00_00, 24), (0x00_ff_00_00, 16), (0x00_00_ff_00, 8), (0x00_00_00_ff, 0))
    )
