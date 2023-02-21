# *** Task 1

# 'users exist'

# *** Task 2

pythonists = ["Bush", "Buffon", "Joe", "Mike", "Flan", "John", "Vardan", 'Azat']

name = 'Azat'

if name not in pythonists:
  pythonists.append(name)

print(name, '1.1')

pythonists_length = len(pythonists)

if pythonists_length > 5 and pythonists_length < 7:
  print(pythonists_length)
elif pythonists_length < 5:
  print('appended new user', '1.2')
  pythonists.append('new user')
else:
  if pythonists_length > 7:
    print('user removed', '1.2')
    pythonists.remove(name)

# *** Task 3

i = 1
while i < 21:
  if i % 2 == 0:
    print(i, 'Task 3')
  i += 1

# *** Task 4

i = 21
while i > 1:
  i -= 1
  if i == 17:
    continue
  print(i, i ** 2, 'task 4')


# *** Task 5

i, count = 2, 0
while i < 50:
  if count == 10:
    break
  if i % 3 == 0:
    count += 1
    print(i, 'task 5')
  i += 1

# Research
# 	1. Ինչպես է աշխատում else-ը while-ի հետ
# ete while-i paymany chi bavararum mtnuma else, aysinqn ete infinit loop-i mej chnknenq mi angam kashxati else

