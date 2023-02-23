# *** Task 1

# *** 1.1 start
def get_keys(file_path='db.txt'):
  with open(file_path) as file:
    keys = file.readlines()[0].strip()
  return keys.split(',')

def get_users_data(file_path='db.txt'):
  with open(file_path) as file:
    data = file.readlines()[1:]
  return [values.strip().split(',') for values in data]

def create_users(keys, data):
  users = []

  for values in data:
    users.append(dict(zip(keys, values)))
  return users

users = create_users(get_keys(), get_users_data())

print(users, '1.1')

# *** 1.1 end



# ### 1.2 start

def add_user_to_current_list(users, **kwargs):
  users.append(kwargs)

my_data = {
  'first_name': 'Azat', 'last_name': 'Aslanyan', 'age': '26', 'profession': 'quick learner', 'country': 'Armenia',
  'favorite_film': 'Gattaca', 'favorite_singer': 'chgidem', 'favorite_chips': 'lays'
}

add_user_to_current_list(users, **my_data)

print(users, 'task 1.2')
# ### 1.2 end



# ### 1.3 start
def add_data_to_db(new_data, db_path='db.txt'):
  with open(db_path, 'a') as db:
    db.write(f'\n{new_data}')

add_data_to_db(','.join(users[-1].values()))
# ### 1.3 end

# *** Task 2

get_number = lambda val: val[0] if not isinstance(val[0], list) else get_number(val[0])

print(get_number([[[[[10]]]]]), 'task 2')


# *** Task 3

def get_sum(numbers_list, total=0, idx=0):
  if idx == len(numbers_list):
    return total

  val = numbers_list[idx]
  total = total + val if not isinstance(val, list) else get_sum(val, total, 0)

  return get_sum(numbers_list, total, idx + 1)


print(get_sum([1, 2, [3, 4], 5, [6, [7, 8], 9], 10]), 'task 3')

# Research
#	1.	lambda functions

# lambda-nery anonymous functionner en voronq karanq veragrenq nayev popoxakanneri ev ogtagorcenq,
# ira mech statementner kam looper chenq kara anenq ete mi toxani chi, ete uzumenq mi qani tox grenq
# karanq () senc pakagcer ogtagorcenq, u hamel karanq iran grenq u texum kanchenq orinak `

# (lambda a, b: print(a + b))(1,2)

