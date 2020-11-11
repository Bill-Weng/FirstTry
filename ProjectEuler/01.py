def foo(value):
  items = [i for i in value if (value%3 == 0 and value%5 == 0)]
  print(sum(items))
