from .auth_helpers import get_users
from .decorators import filter_users_decor, count_function_executed_time
@filter_users_decor
@count_function_executed_time
def login(email, password):
  users = get_users()

  for user in users:
    if email == user['email']:
      if password == user['password']:
        print('Login successful!')
        return user
      else:
        raise ValueError('Incorrect password.')

  raise ValueError('User not found.')
