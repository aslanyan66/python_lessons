from functools import wraps
from time import time
from .auth_helpers import get_users


def filter_users_decor(func):
  ''' The func must return user that wrapper can have user role and filter users.'''

  @wraps(func)
  def wrapper(*args):
    try:
      user = func(*args)
      if user['role'] == 'user':
        return user

      users = get_users()

      if user['role'] == 'admin':
        return list(filter(lambda user: user['role'] == 'admin' or user['role'] == 'user', users))
      return users
    except ValueError as error:
      print(error)

  return wrapper


def count_function_executed_time(func):
  def wrapper(*args):
    start = time()
    result = func(*args)
    end = time()
    exec_time = end - start
    print(exec_time)
    return result

  return wrapper


def country_restrict(countries):
  def decorator(func):
    def wrapper(**data):
      user_country = data['country']
      if user_country not in countries:
        raise ValueError('Please fill valid country')

      return func(**data)

    return wrapper

  return decorator
