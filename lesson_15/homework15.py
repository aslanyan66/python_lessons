# *** Task 1
data = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
symmetric_items = list(filter(lambda item: item == item[::-1], data))

print(symmetric_items, 'task 1')

# *** Task 2

def custom_map(cb, *args):
  return (cb(*items) for items in zip(*args))

print(list(custom_map(lambda x: x * 2, [1,2,3,4,5,6])), 'task 2')
print(list(map(lambda x: x * 2, [1,2,3,4,5,6])), 'task 2')

# *** Task 3

numbers = [1, 2, 5, 70, 4, 8, 50, 44]

# *** task 3.1
def get_max_num(numbers):
  max_num = float('-inf')
  for num in numbers:
    max_num = num if max_num < num else max_num
  return max_num

print(get_max_num(numbers), 'Task 3.1')


# *** Task 3.2

from functools import reduce

max = reduce(lambda max, item: item if max < item else max, numbers, float('-inf'))

print(max, 'Task 3.2')