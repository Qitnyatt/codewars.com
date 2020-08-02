# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/coffeescript

dirReduc = (arr) ->
  opposition = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
  }
  i = 0
  while i < arr.length
    if arr[i]? and arr[i + 1]? and arr[i] is opposition[arr[i + 1]]
      arr.splice i, 2
      i -= 1
      continue
    i++
  arr