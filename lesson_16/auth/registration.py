from .auth_helpers import is_exist_user, check_user_data
from .paths import users_relative_path
from .decorators import country_restrict

@country_restrict(['Armenia', 'USA', 'Germany', 'France'])
def registration(**user_data):
  if is_exist_user(user_data['email']):
    raise ValueError('User is already exist.')

  check_user_data(**user_data)
  with open(users_relative_path, 'a') as users:
    user_to_string = '\n{first_name},{last_name},{email},{password},{age},user,{country}'
    users.write(user_to_string.format(**user_data))
    return True
  print(error)
