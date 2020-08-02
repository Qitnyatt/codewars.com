# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/coffeescript

validParentheses = (parentheses) ->
  counter = 0
  for ch in parentheses
    if counter <= -1
      break
    if ch == ')'
      counter -= 1
    if ch == '('
      counter += 1
  return  if counter == 0 then true else false
