# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python


def validate_battlefield(field):
    field_width = len(field[0])
    field_height = len(field)

    field_outlined = [[0] * (field_width + 2)]
    for y in range(field_height):
        field_outlined.append([0] + field[y] + [0])
    field_outlined.append([0] * (field_width + 2))

    state = {
        'battleship': {
            'length':              4,
            'required':            1,
            'found':               0,
            'invariants':          [],
            'outlined_invariants': [],
        },
        'cruiser':    {
            'length':              3,
            'required':            2,
            'found':               0,
            'invariants':          [],
            'outlined_invariants': [],
        },
        'destroyer':  {
            'length':              2,
            'required':            3,
            'found':               0,
            'invariants':          [],
            'outlined_invariants': [],
        },
        'submarine':  {
            'length':              1,
            'required':            4,
            'found':               0,
            'invariants':          [],
            'outlined_invariants': [],
        },
    }

    for ship in state:
        state[ship]['invariants'].append([[1 for _ in range(state[ship]['length'])]])
        need_generate_invariants = False
        if state[ship]['length'] != 1:
            need_generate_invariants = True
        if need_generate_invariants:
            state[ship]['invariants'].append([list(x) for x in zip(*state[ship]['invariants'][0])])

    for ship in state:
        for ship_invariant in state[ship]['invariants']:
            ship_width = len(ship_invariant[0])
            ship_height = len(ship_invariant)
            area = [[0 for _ in range(0, 1 + ship_width + 1)] for _ in range(0, 1 + ship_height + 1)]
            ship_outlined = area
            for y in range(1, ship_height + 1):
                for x in range(1, ship_width + 1):
                    ship_outlined[y][x] = ship_invariant[y - 1][x - 1]
            state[ship]['outlined_invariants'].append(ship_outlined)

    for ship in state:
        for _ in range(state[ship]['required']):
            found = False
            for outlined_invariant in state[ship]['outlined_invariants']:
                if found:
                    break
                ship_width = len(outlined_invariant[0])
                ship_height = len(outlined_invariant)
                for y in range(0, 1 + field_height + 1 - ship_height + 1):
                    for x in range(0, 1 + field_width + 1 - ship_width + 1):
                        search_area = []
                        for dy in range(y, min(y + ship_height, 1 + field_height + 1)):
                            row = []
                            for dx in range(x, min(x + ship_width, 1 + field_width + 1)):
                                row.append(field_outlined[dy][dx])
                            search_area.append(row)
                        if search_area == outlined_invariant:
                            state[ship]['found'] += 1
                            for dy in range(y, min(y + ship_height, 1 + field_height + 1)):
                                for dx in range(x, min(x + ship_width, 1 + field_width + 1)):
                                    field_outlined[dy][dx] = 0
                            found = True
            if not found and not (state[ship]["required"] == state[ship]["found"]):
                return False

    return all([state[ship]['found'] == state[ship]["required"] for ship in state])
