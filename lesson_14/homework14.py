# *** Task 1
# function generator-y petqa kanchenq vor unenaq generator object isk list comprehension-@ arden veradarcnuma et objectic

# *** Task 2

# karanq functioni mech tenanq yield ka te che,
# type(some_func()) senc orinak
# karanq inspect modul@ qashenq u vrayic isgeneratorfunction-@ kanchenq kta True or False

# *** Task 3

def get_fib_num():
  x, y = 0, 1

  while True:
    current = x + y
    yield x
    x, y = y, current

fib_iter = get_fib_num()

for i in range(0):
  print(next(fib_iter), 'Task 3')

# Task 4

def custom_range(start,end=None,step=1):
  if end is None:
    end = start
    start = 0

  while start < end:
    yield start
    start += step

my_gen = custom_range(10,20,2)

for i in my_gen:
  print(i, 'task 4')


# *** Task 5

def is_symmetric(text):
  for i in range(len(text) // 2):
    if text[i] != text[len(text) - i - 1]:
      return False
  return True

print(is_symmetric('abccaba'), 'Task 5')

# *** Task 6

x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
y = { key: is_symmetric(key) for key in x }
print(y, 'Task 6')


# Research
# 	1.	__iter__ method:
# tvyal objecty darcnuma iterator, et ena inchvor for in i jamanak kanchvuma iterable-i vrayic
# 	2.	Գրեք մեր անցած iterable data type-երը:
# str, list, set, frozenset, tuple, dict
# 	3.	Գրեք մեր անցած sequence data type-երը:
# str, list, set, frozenset, tuple
# 	4.	Գրեք sequence-ի և iterable-ի տարբերությունները:
# voch bolor iterable-nernen sequence bayc bolor sequence-nery iterable en
