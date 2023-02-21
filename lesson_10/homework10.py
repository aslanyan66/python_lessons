# *** Task 1

my_name = 'name'
def f1():
  global my_name
  my_name = 'Hello'
f1()
print(my_name)

# *** Task 2

users = ["Lilit", "Aren", "Janna", "Janna", "Janna", "Janna", "Luiza", "Janna", "Armen", "Lilit"]
def get_repeated_items_list(sequence_object):
  if type(sequence_object) == 'int':
    return 'please send sequence object'
  items_dict = {}
  result = []

  for item in sequence_object:
    if item not in items_dict:
      items_dict[item] = 1
      continue
    items_dict[item] += 1
    result.append(item)
  return result

print(get_repeated_items_list(users))

def f(sequence_object):
  unique_items = set()
  result = set()

  for item in sequence_object:
    if item in unique_items:
      result.add(item)
    else:
      unique_items.add(item)

  return list(result)

# *** Task 3

def get_sum_digits(num):
  sum = 0
  while num:
    sum += num % 10
    num = num // 10
  return sum

print(get_sum_digits(12))

# *** Task 4

def get_prime_numbers_list(n=100):
  primes_list = [1]
  for i in range(2, n):
    is_prime = True
    for j in range(2, i // 2 + 1):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      primes_list.append(i)
  return primes_list

print(get_prime_numbers_list())

# *** Task 5

def get_current_fib(num):
  if num <= 0:
    return 'Enter positive number'

  prev, current = 0, 1

  while num > 1:
    next_fib = prev + current
    prev = current
    current = next_fib
    num -= 1
  return prev

print(get_current_fib(5))


# Research
#	1.	Python Function Annotations

# def repeat_string(s: str, n: int = 2) -> str:
#   return s * n

# function annotationnerov karox enq argumentnerin type-er tal u tal te function-@ incha veradarcnelu,
# bayc sxal argument talu depqum error chenq stanum
# annotationnerov karoxanum enq type-er tanq mer popoxakannerin vory aveli readable kdarcni mer code-y, khushi vor depqum incha linelu

#	2.	Function-ի parametrs *args, **kwargs

# *args-i depqum stanum enq tuple, vorpes functioni argument bayc kancheluc ansahman argumentner karanq dnenq
# **kwargs-i depqum vorpes dict enq stanum functionum bayc kancheluc talisenq senc f(name="flan")



















