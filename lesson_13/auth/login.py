def login():
  email, password = [input(f'Enter your {field}. ') for field in ['email', 'password']]
  with open('users.txt') as users_file:
    existing_users = users_file.readlines()[1:]

  for user in existing_users:
    current_email, current_password, first_name, last_name = user.strip().split(',')

    if email == current_email:
      if password == current_password:
        print('Login successful.')
        return f'Hello {first_name} {last_name}!'
      else:
        raise ValueError('Incorrect password!')

  raise ValueError('User not found!!!')
