# *** Task 1

my_data = {
  'first_name': 'Azat', 'last_name': 'Aslanyan', 'age': '26', 'profession': 'quick learner', 'country': 'Armenia',
  'favorite_film': 'Gattaca', 'favorite_singer': 'chgidem', 'favorite_chips': 'lays'
}

# *** 1.1 start

def generate_dict_from_db():
  with open('db.txt') as db:
    keys = db.readline().strip().split(',')
    result = [dict(zip(keys, line.strip().split(','))) for line in db]

  result.append(my_data)
  return result


users = generate_dict_from_db()
print(users, '1.1')


# *** 1.1 end

# *** 1.2 start

updated_users = (lambda users, **kwargs: [{**user, **kwargs} for user in users])(users, firend='flan', friend_of_friend='fstan')
print(updated_users,'1.2')

# *** 1.2 end

# *** 1.3 start

def write_users_in_db(users, path='db.txt'):
  keys = ','.join(users[0].keys())
  values = [','.join(user.values()) for user in users]
  data = '\n'.join([keys, *values])

  with open(path, 'w') as db:
    db.writelines(data)
  print('See 1.3 in db.txt')

write_users_in_db(updated_users)

# *** 1.3 end


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

