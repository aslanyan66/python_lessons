# def auth(func):
#   def wrapp(name):
#     print("first decorator started")
#     func(name)
#     print("first decorator finished")
#
#   return wrapp
#
#
# def second_auth(func):
#   def wrapp(name):
#     print("second decorator started")
#     func(name)
#     print("second decorator finished")
#
#   return wrapp
#
#
# @auth
# @second_auth
# def login(name):
#   print(f'user {name} logged in')
#
#
# login('Jasper')


# def auth(func):
#   def wrapp(name):
#     print("first decorator started")
#     func(name)
#     print("first decorator finished")
#
#   return wrapp
#
#
# def second_auth(func):
#   def wrapp(name):
#     print("second decorator started")
#     func(name)
#     print("second decorator finished")
#
#   return wrapp
#
#
# def login(name):
#   print(f'user {name} logged in')
#
#
# wrapped_login = auth(second_auth(login))
# wrapped_login('Jasper')


# def auth_wrapp(arg1, arg2):
#   def auth(func):
#     def wrapp(name):
#       print("auth package ", arg1)
#       func(name)
#       print("auth package ", arg2)
#
#     return wrapp
#
#   return auth
#
#
# @auth_wrapp("started", "finished")
# def login(name):
#   print(f'user {name} logged in')
#
#
# @auth_wrapp("started", "finished")
# def register(name):
#   print(f'user {name} registered')
#
#
# login("Vardan")


# import datetime
#
# now = datetime.datetime.now()
# print("Current time is:", now.time())


# def say_hello():
#   print('hello')
#
# def decor(func):
#   def wrapper():
#     print('barlus')
#     func()
#     print('hajox')
#
#   return wrapper
#
#
# hello = decor(say_hello)
#
# hello() # barlus hello hajox