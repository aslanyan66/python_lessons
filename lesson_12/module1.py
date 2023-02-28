# is prime number

def is_prime_num(num):
  for i in range(2, num // 2 + 1):
    if num % 2 == 0:
      return False

  return True



