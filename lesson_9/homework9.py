# *** Task 1

def print_data(name='Vaspur', lastname='Smith', age=61):
  print(f'Hello my name is {name}, my last name is {lastname}, I am {age} years old')


# *** Task 2

def change_char(text='', old_character='', new_chararcter=''):
  result = ''
  for char in text:
    result += char if char != old_character else new_chararcter
  return result

# *** Task 3

def write_in_file(list_of_texts, file_name='text.txt'):
  with open(file_name, 'w') as text_file:
    text_file.write('\n'.join(list_of_texts))
print(write_in_file(['s','s','s']))

# *** Task 4

def is_prime(num):

  '''Gets one arrgument as integer and cheks is it prime number. Returns True or False'''
  for i in range(2, num // 2 + 1):
    if num % i == 0:
      return False
  return True

print(is_prime(11))

#	Research
#	1. Ինչպես գրել function-ի documentation և կանչել help function-ով:
# is-prime function-i hamar grelem
# help(is_prime)
