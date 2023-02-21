# 1.  Ունենք սենց dict
#			user = {
#				'name':'Jarviz',
#				'age' : '100',
#				'professions':['robot', 'dancer']
#				'test_result':[14,5,8,99,12,2,3,5,4]
#			}
#			
#	    1.1 Ինչպես կարող ենք տպել 'robot'-ը ու փոխել 'dancer'-ը:
#	    1.2 Սորտավորեք test_result-ը ըստ նվազման:

user = {
    'name': 'Jarviz',
    'age': '100',
    'professions': ['robot', 'dancer'],
    'test_result': [14, 5, 8, 99, 12, 2, 3, 5, 4]
}

print(user['professions'][0])
user['professions'][1] = 'spam'
user['test_result'].sort(reverse=True)

#	2. Ունենք սենց dict
#			fruits = {
#				"banana": 4,
#				"apple": 2,
#				"orange": 1.5,
#				"pear": 3
#			}
#		2.1 Հաշվել բոլոր մրգերի գումարը
#		2.2 Ավելացրեք ձեր սիրած միրգը ու ինչքան եք իրան գնահատում

fruits = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(sum(fruits.values()))
fruits['cabbage'] = 2

# 3.
#		[
#			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
#			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
#		]

#		3.1 Լրացրեք բաց թողնված value-ները ( is_5g-ի արժեքը պետք է լինի bool type-ի )
#		3.2 Ավելացրեք նոր dict արդեն եղած user-երին, օրինակ ՝ {'car':{'model': '', 'type': '', 'max_speed': ''}}
#		3.3 Տպել is_5g-ին ամեն user-ի համար True է թե False
#		3.4 x-ին վերագրեք հետեվյալ պայմանների արդյունքում ստացված արժեքը 
#			age մեծ է 18-ից և is_5g-ին հավասար է True կամ first_name-ի մեջ չկա bill և last_name-ի մեջ չկա gates:
#			Հետո տպեք print('chipavorvac e', x)

persons = [
    {'first_name': '', 'last_name': '', 'age': 15, 'phone': {'brend': '', 'number': '', 'is_5g': ''}},
    {'first_name': '', 'last_name': '', 'age': '', 'phone': {'brend': '', 'number': '', 'is_5g': ''}}
]

persons[0]['phone']['is_5g'] = True
persons[1]['phone']['is_5g'] = False

persons[0]['car'] = {'model': '', 'type': '', 'max_speed': ''}
persons[1]['car'] = {'model': '', 'type': '', 'max_speed': ''}

print(f'user1 ==> {persons[0]["phone"]["is_5g"]} , user2 ==> {persons[1]["phone"]["is_5g"]}')

current_user = persons[0]
x = current_user['age'] > 18 and current_user['phone']['is_5g'] == True or 'bill' not in current_user[
    'first_name'].lower() and not 'gates' in current_user['last_name'].lower()

print('chipavorvac e', x)

#	4. zip()-ի և այլ անհրաժեշտ գործիքների միջոցով ստացեք dict որի key-րը կլինեն ձեր անվան առաջին տառերը իսկ
#	   value-ները հակառակ տառերը, օրինակ ՝ jarvis {'j':'s', 'a':'i', 'r':'v', 'v':'r', 'i':'a', 's':'j'}


my_name = 'jarvis'

print(dict(zip(my_name, my_name[::-1])))

#  1. setDefault()
# setDefault-@ nmana get methodin uxaki ete tvyal property-n chi linum avelacnum dict-i mej tvyal property-in
#  2. fromkeys()
# fromkeys-@ dict-i methoda vor sequence-neri himman vra dict-a karucum arjeqnel veragruma defaultov gnacac@
#  3. Փորձեք կիրառել մեր անցած ֆունկցիաները dict-ի համար և գրեք արդյունքներիը

dc = {'a': 1, 'b': 2, 'c': 3, 'z': 8, 'o': 3}

print(sorted(dc), 'sorted')
print(len(dc))
