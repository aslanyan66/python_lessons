# 1. Ունենք օրինակ users_list = ['Vardan', 'Vazgen', 'Jarviz']
#	1. print արեք list-ի բոլոր անդամները:
#	2. Ինչպես կարող ենք փոխել 'Vazgen'-ը մեկ այլ անունով:

users_list = ['Vardan', 'Vazgen', 'Jarviz']

print(users_list[0], users_list[1], users_list[2])


# 2. Ունենք 2 list 
#    	x = [1,2,3,4,5,6]
#	z = [7,8,9,10,11]
#	Ինչպես կարող ենք իմանանալ դրանց ըդհանուր երկարությունը:

x = [1,2,3,4,5,6]
z = [7,8,9,10,11]

print(len(x + z))

# 3. Նշեք ինչ ընդանուր ֆունկցիաներ գիտեք հաջորդականությունների համար ու ինչ են իրանք վերադարցնում:

# sorted => sortavoruma mer listy veradarcnum nor ref
# len => talisa listi length@
# sum => hashvuma listi tveri gumary, ashxatuma int-eri kam float-neri het

# 4. Ստեղծել երկու input():
#	Առաջինը պետքա ունենա սենց հրավերքի տեքստ - how many words do you want to type?
#	Իսկ երկրորդը պետքա ունենա սենց հրավերքի տեքստ - write a word
#	Արդյունքում պետքա print անենք մեր երկրորդ input-ից ստացած բառը բազմապատկած առաջին input-ից ստացած քանակությամբ:

input_one = input('how many words do you want to type? ')
input_two = input('write a word ')

print(input_two * int(input_one))

# 5. Ունենք users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
#	Հարկավոր է input()-ի միջոցով ավելացնել նոր user-ի, որից հետո պետք է տպել հին(исходный) users_list-ը և նոր users_list-ը:

users_list2 = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
new_user_list2 = users_list2 + [input('Add new user ')]

print(users_list2, new_user_list2)



# 6. Ունենք users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
#	Ստեղծել input(), որը կունենա սենց հրավերքի տեքստ 
#		'Your users ["Vazgen", "Chris Tacker", "Nikola Tesla"]'
#		'who do you want to remove ?'
#	Հետո գրեք են user-ի անունը որին ուզում եք հեռացնել:
#	Արդյունքում ստանանք սենց տեքստ
#		'User NIKOLA TESLA(մեծատառ) is removed'
#        'Your users ["Vazgen", "Chris Tacker"]'


users_list3 = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
rm_user_index = users_list3.index(input(f'Your users are {users_list3}, who do you want to remove? '))
rm_user = users_list3.pop(rm_user_index)
print(f'User {rm_user} is removed.Your users are {users_list3}')



# 7. Ունենք numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    Գտնել զույգ թվերի գումարը:

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(numbers_list[1:][::2]))


# 1. list-ի որ մեթոդով կարող ենք գտնել տրված արժեքի index-ը:
# index
# 2. Ինչ է անում del արտահատությունը ու ինչով է տարբերվում remove()-ից:
# del aneluc index enq talis remove method-i jamanak value
