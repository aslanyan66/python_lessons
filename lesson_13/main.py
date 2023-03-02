# *** Task 1

# interpretatory kdadari ashxatel

# *** Task 2

# raise-ov , assert


# *** Task 3

import auth

auth_action = input('login or registration? ')
auth_method = getattr(auth, auth_action)

try:
  auth_method()
except Exception as err:
  print(err)

#   Research
#
# 1.  Ինչպես կարող ենք raise-ի միջոցով փոխանցել message exception-ին:

# raise ExceptionType('spam')

# 2.	Ուսումնասիրեք math package-ը և դուրս գրեք 3 ձեզ դուր եկած և ձեր կարծիքով ամենաօգտակար method-ները:

# math.sqrt() armata hanum
# math.gcd() 2 tvi amenamec bajanararna talis
# math.isnan() stuguma arjeqy tiv chi te che , aysinqn ete not a number-a True-a talis u hakaraky