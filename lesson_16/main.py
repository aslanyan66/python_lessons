import os
import sys
import auth

# Task 1

# Task 1.1

current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, 'auth')
sys.path.append(relative_path)

login_result = auth.login('bushjr@gmail.com', 'bush1234')
print(login_result, ' login_result')

# 1.1 end

# 1.2 is in auth/decorators

# Task 2
# first_name,last_name,email,password,age,role,country

try:
  auth.registration(
    **{'first_name': 'Azat', 'last_name': 'Aslanyan', 'email': 'hello@gmail.com', 'password': 'bush1234', 'age': 25,
       'country': 'Armenia'}
  )
except ValueError as error:
  print(error)

# Research
# 	1.	functools module - wraps
# wraps-@ decoratora mer decoratric veradarcvox wrapper-i hamar vorpesi wrapper@ vercni decoratrin argumentov ekac functioni metadatan,
# orinak funct.__name__, kam functioni description@ vor help-ov karananq tenanq

# 	2.	time module
# time moduly built in modula jamanaki het manipulyacyaner anelu, timerner sarqelu, jamanak chapelu
