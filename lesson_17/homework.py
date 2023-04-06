import re
from decimal import Decimal
from functools import reduce

# *** Task 1

pattern = r'[A-Z][a-z]*[.][A-Z][a-z]+'
text = 'S.Paloyan Vardan Vardanyan Miqayel_Abrahamyan H.Stepanyan P.Petrosyan_5 J.Blade'

names = re.findall(pattern, text)
print(names, 'Task 1')

# *** Task 2

pattern = r'[$]+\d+[,]+[\d]+'
text = '''
        There are many variations of passages of Lorem Ipsum available, but the $6700 majority have suffered alteration 
        in some form,
        by injected humour, or randomised words which don't look even slightly  believable. If you are going to use 
        a passage $3,200
        of Lorem Ipsum, 8,200 you need to be sure there isn't anything embarrassing hidden in the middle of text. 
        All $5,200 the Lorem Ipsum
        generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator 
         $3,200.00 on the Internet. 
        It uses a dictionary of over 200 Latin words, combined with a handful of $5200  model sentence structures,
         to generate Lorem Ipsum which looks reasonable.
        The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
		  '''
prices = re.findall(pattern, text)
print(prices, 'Task 2.1')

prices = map(lambda price: float(price[1:].replace(',', '.')), prices)
print(reduce(lambda aggr, price: aggr + price, prices, 0), 'task 2.2')

# *** Task 3

pattern = r'https?://www.[a-z\d]+.[a-z]{3}'
text = 'https://www.youtube.com ab-3.com http://translate.google.ru www.github.com https://www.w3schools.com https://www.python.org instagram.com www.fb.com'

links = re.findall(pattern, text)
print(links, 'Task 3')

# *** Task 4

# *** Task 4.1

from emails import generate_emails

def check_email(email, pattern=None, current_task_name='4.2'):
  if pattern == None:
    pattern = r'^[a-z-_.\d]{2,}@[a-z]{2,}\.[a-z]{2,4}$'
    current_task_name = '4.1'
  result = bool(re.match(pattern, email))

  print(result, email, f'Task {current_task_name}')
  return bool(re.match(pattern, email))


valid_emails = generate_emails(5, True) # valid for task 4.1
invalid_emails = generate_emails(5, False)

# Invalid cases for test 4.1
# for invalid_email in invalid_emails:
#   check_email(invalid_email)

# Valid cases for test 4.1
# for valid_email in valid_emails:
#   check_email(valid_email)


# *** Task 4.2

pattern = '^[a-z]{5}\@[a-z]{2,4}.ru$'

# Invalid cases for test 4.2
# for invalid_email in invalid_emails:
#   check_email(invalid_email, pattern)

# valid case for 4.2
# check_email('aaaaa@bbbk.ru', pattern)


# Research
# 	python re compile

# erpvor nuyn pattern@ mi qani angam petqa ogtagorcenq aveli lava ogtvenq re.compile methodic , vory veradarcnuma regex object,
# vornel ir hertin heto aveli optimala ashxatum

# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# result = pattern.match('123-456-7890')



