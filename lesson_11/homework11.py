# *** Task 1

def get_users_data(file_path):
  with open(file_path) as file:
    data = file.readlines()[1:]
  return [values.strip().split(',') for values in data]


def get_keys(file_path):
  with open(file_path) as file:
    keys = file.readlines()[0].strip()
  return keys.split(',')


def add_data_to_db(new_data, db_path='db.txt'):
  with open(db_path, 'a') as db:
    db.write(f'\n{new_data}')


def create_users(keys, data):
  users = []

  for values in data:
    users.append(dict(zip(keys, values)))
  return users


def add_user(users, **kwargs):
  users.append(kwargs)
  print(kwargs.values(), 'a')
  add_data_to_db(','.join(kwargs.values()))


my_data = {
  'first_name': 'Azat', 'last_name': 'Aslanyan', 'age': '26', 'profession': 'quick learner', 'country': 'Armenia',
  'favorite_film': 'Gattaca', 'favorite_singer': 'chgidem', 'favorite_chips': 'lays'
}

users = create_users(get_keys('db.txt'), get_users_data('db.txt'))
add_user(users, **my_data)

# *** Task 2

get_Number = lambda val: val[0] if not isinstance(val[0], list) else get_Number(val[0])

print(get_Number([[[[[10]]]]]))


# *** Task 3

def get_sum(numbers_list, total=0, idx=0):
  if idx == len(numbers_list):
    return total

  val = numbers_list[idx]
  total = total + val if not isinstance(val, list) else get_sum(val, total, idx + 1)

  return get_sum(numbers_list, total, idx + 1)


print(get_sum([1,2]))


# Research
#	1.	lambda functions

# lambda-nery anonymous functionner en voronq karanq veragrenq nayev popoxakanneri ev ogtagorcenq,
# ira mech statementner kam looper chenq kara anenq ete mi toxani chi, ete uzumenq mi qani tox grenq
# karanq () senc pakagcer ogtagorcenq, u hamel karanq iran grenq u texum kanchenq orinak `

# (lambda a, b: print(a + b))(1,2)

