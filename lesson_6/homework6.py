# *** Task 1
x = {1, 2, 4, 5, 6}
y = {5, 6, 7, 8, 9}

print(x - x.symmetric_difference(y))
print(x - y)
print(x.difference(y))

# ***

# *** Task 2

print(x - x.intersection(y))

# ***

# *** Task 3

# arajin argument@(file pathy) partadira mnacacy voch,defaultov r-a gnum erkrordin

# *** Task 4

file_1_path = 'file_1.txt'
file_2_path = 'file_2.txt'

with open(file_1_path, 'a') as file_1:
  file_1.write('File one have created.\n')
  file_1.write('Have added some text to file one.')
  file_1.close()

with open(file_2_path, 'a') as file_2:
  file_2.write('File one have created.\n')
  file_2.write('Have added some text to file one.')
  file_2.close()

with open(f"{input('Which file do you want to read?')}.txt", 'r') as current_file:
  print(current_file.read())
  current_file.close()

# ***

# # *** Task 5

user1, user2 = [
  {
    'first_name': 'Jorj',
    'last_name': 'Bush',
    'age': 55
  },

  {
    'first_name': 'James',
    'last_name': 'Bond',
    'age': 100
  }
]

with open('users_file.txt','w') as users_file:
  users_file.write(f'user 1: first_name = {user1["first_name"]}, last_name = {user1["last_name"]}, age = {user1["age"]}\n'
                   f'user 2: first_name = {user2["first_name"]}, last_name = {user2["last_name"]}, age = {user2["age"]}')
  users_file.close()


# Research
#	1. isdisjoint() մեթոդը

# isdisjoint methodov stugumend set-erin u ete erku setery chunen yndhanur itemner stanum enq True hakarak depqum False

set1 = {30, 20, 10}
set2 = {3, 2, 1}

result = set1.isdisjoint(set2)
print(result)

#	2. remove()-ի ու discard()-ի տարբերությունը

# ete remove enq anum item u chi linum seti mech error enq stanum discardi depqum che