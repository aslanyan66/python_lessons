from .paths import users_relative_path
def get_users():
  with open(users_relative_path) as users:
    users_data = users.readlines()
    keys = users_data[0].strip().split(',')
    users = users_data[1:]
  return list(map(lambda user: dict(zip(keys, user.strip().split(','))), users))


def is_exist_user(email):
  with open(users_relative_path) as users:
    for user in users:
      current_email = user.strip().split(',')[2]

      if current_email == email:
        return True

  return False


def is_valid_value(name, min_length=4, max_length=30):
  name_length = len(name)
  return True if name_length >= min_length and name_length <= max_length else False

def check_user_data(**user_data):
  first_name, email, password = user_data['first_name'], user_data['email'], user_data['password']
  last_name, age, country = user_data['last_name'], user_data['age'], user_data['country']

  error_message = ''

  print(not is_valid_value(first_name))

  if not is_valid_value(first_name) or not is_valid_value(last_name):
    error_message = 'First Name and Last Name must have at least 4 char and maximum 30'
  elif email[-10:] != '@gmail.com':
    error_message = 'Please wright correct gmail'
  elif not is_valid_value(password, 8):
    error_message = 'Password must have at least 8 char and max 30.'
  elif age < 0 or age > 112:
    error_message = 'Please write correct age.'
  elif not is_valid_value(country, 3, 25):
    error_message = 'Please write correct country.'

  if error_message:
    raise ValueError(error_message)

  return True