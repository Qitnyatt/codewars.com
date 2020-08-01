# https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0/train/python


def my_first_interpreter(code):
    result = []
    cell = 0
    for cmd in code:
        if cmd == '+':
            cell = (cell + 1) % 256
        elif cmd == '.':
            result.append(chr(cell))
        else:
            pass
    return ''.join(result)
