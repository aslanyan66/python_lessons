# *** Task 1
import sys

# math , copy ,

# *** Task 2

# de ete * import anenq tvyal moduli bolor methodnery kgan global scope u kara conflikt lini ete nuyn anunov methodner unenanq,
# bayc chem hishum meky mekin override-a anum te erroa talis

# *** Task 3

# __init__.py file-ը naxatesvaca packagi papki mech vorpes glxavor talu hamar vortexic voroshum enq inch modulner
# petqa hasaneli linen package-ic durs


# *** Task 4

import module1

# __name__ es popoxakanin dimum enq vor imananq vor moduli mej enq isk mer glxavor file-@ vortexic sksum enq anvanvuma __main__

# *** Task 5

from sys import argv as arguments

users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza"]
type_for_convert_list = arguments[1] if len(arguments) > 1 else 'list'

def print_users(users, frequency_type):
  frequency_methods = {
    'list': list,
    'tuple': tuple,
    'str': str,
    'set': set,
    'frozenset': frozenset
  }
  frequency_type = frequency_type.lower()

  if frequency_methods.get(frequency_type, False):
    return frequency_methods[frequency_type](users)
  return users

print(print_users(users, type_for_convert_list), 'task 5')

# *** Task 6

from module1 import is_prime_num

print(is_prime_num(31), 'task 6')


# *** Task 7

import im_chashakov

im_chashakov.get_hamadrutyun1()
im_chashakov.get_hamadrutyun2()

# Research

# 1. sys module-ի path attribute-ը

# sys.path-@ lista stringneri vori mech current file-i pathna u pythoni modulneri pathery
# erp import enq anum sys.path-i meji patheri meja interpretatory mtnum vor hamapatasxan moduly gtni

# 2. sys module-ի argv attribute-ը

# sys.argv veradarcnuma list vortex current modulna u run aneluc tvac argumenty
