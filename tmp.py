try:
  a = input("type a number")
  b = input("type b number")
  a = int(a)
  b = int(b)
  print(a/b)
except (ZeroDivisionError,ValueError):
  print("０を入れないで")