# https://www.codewars.com/kata/58708934a44cfccca60000c4/train/python

import re


def highlight(code: str) -> str:
    code = re.sub(r'(F+)', r'<span style="color: pink">\1</span>', code)
    code = re.sub(r'(L+)', r'<span style="color: red">\1</span>', code)
    code = re.sub(r'(R+)', r'<span style="color: green">\1</span>', code)
    code = re.sub(r'(\d+)', r'<span style="color: orange">\1</span>', code)
    return code
