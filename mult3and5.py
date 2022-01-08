def mult3and5():
  total = 0
  for i in range(0,1000):
    if i % 3 == 0:
      total = total + i
    if i % 5 == 0:
      total = total + i
      if i % 15 == 0:
        total = total - i
  print(total)