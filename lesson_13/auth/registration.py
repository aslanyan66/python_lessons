def registration():
  email, password, first_name, last_name = [input(f'Enter your {field}. ') for field in ['email', 'password', 'first_name', 'last_name']]
  with open('users.txt', 'r+') as users_file:
    existing_users = users_file.readlines()[1:]

    for user in existing_users:
      current_email = user.strip().split(',')[0]
      if current_email == email:
        raise ValueError('Email address is already in use')

    new_user = f'{email},{password},{first_name},{last_name}\n'
    users_file.write(new_user)
    print('Registration successful.')