for x in range (7):
  if x < 4:
    d = 3 - x
  else:
    d = x - 3
  for y in range(7):
    if y >= d and y <= 6 - d and (y - d) % 2 == 0:
      print("*", end= " ")
    else:
      print(" ", end= " ")
  print()
