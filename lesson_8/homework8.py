# *** Task 1

last_names = ['Adams', 'Allen', 'Brooks', 'Davidsonyan', 'Sargsyan', 'Jenkins']
armenian_last_names = []

index = 0
while index < len(last_names):
  lastname = last_names[index]
  if lastname[-3:].lower() == 'yan':
      armenian_last_names.append(lastname)
  index += 1

print(armenian_last_names)

# *** Task 2

long_word, char_to_find, count = 'arevachachapaylatakum', 'a', 0

if long_word.find(char_to_find) != -1:
  for char in long_word:
    if char == char_to_find:
      count += 1

print(count, 'count')

count, find_index = 0, long_word.find(char_to_find)


while find_index != -1:
  count += 1
  find_index = long_word.find(char_to_find, find_index + 1)

print(count, 'count')

# *** Task 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

range_for_alphabet = (range(1, len(alphabet) * 2, 2))
zipped_alphabet = zip(alphabet, range_for_alphabet)
alphabet_to_dict = dict(zipped_alphabet)

print(alphabet_to_dict)

# *** Task 4

num = 5
factorial = 1

while num > 1:
  factorial *= num
  num -= 1
print(factorial)

num = 5
factorial = 1

for num in range(2, num + 1):
  factorial *= num
  num -= 1
print(factorial)


# *** Task 5

for index in range(0, len(alphabet) // 2):
  alphabet[index], alphabet[-index - 1] = alphabet[-index - 1], alphabet[index]
  index -= 1

print(alphabet)

# Research
# 	1. enumerate() function

# enumerate returna anum iterable voric karanq stananq mer uzac hajordakanutyuny kam dict

# fruits = ["apple", "banana", "cherry"]
# indexed_fruits = enumerate(fruits)
# print(indexed_fruits)


