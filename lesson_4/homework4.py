import copy
# 1. Նշեք copy-ի ու deepcopy-ի տարբերությունը:

# copy-i Objecti vrayic vor kanchum enq copy methody et shallow copy-a anum isk deepy xory))

# 2. Ունենք սենց list x = [1,2,5, [8,9,10]]
#   Վերագրեք y-ին x այնպես, որ x-ի յուրաքանչյուր index-ը փոխելուց y-ը չփոխվի (առանց օգտագործելու deep_copy):

x = [1,2,5, [8,9,10]]
y = x[0:3] + [copy.copy(x[3])]

# 3. Ունենք սենց մի հատ tuple - ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
#   Ինչպես կարանք ավելացնենք 'kiraki'-ին ['Shb']-ի հետ նույն լիստում և բացատրեք թե ինչու error չենք ստանում:

tp = ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
tp[5].append('kiraki')

# vorovhetev tuple-i tvyal indexy lista handisanum isk listi vra karanq avelacnenqel jnjenqel

# 4. Ունենք փոփոխականներ
#	name = 'My name'
#	last_name = 'My last name'
#	patronymic = 'My father name'

#	3 վերագրումները գրեք մեկ տողով:

name, last_name, patronymic = 'My name', 'My last name', 'My father name'

# 5. Ունենք սենց users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
#	Ինչպես կարող ենք փոխել users_tuple-ի ինչ որ value:

users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
users_tuple = list(users_tuple)
users_tuple[0] = 'Hello'
users_tuple = tuple(users_tuple)


# 6. Նախ արեք resaearch-ի հատվածը որպեսզի կարողանաք անել տնայինը

#	Ունենք users_list = [
#			"Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
#			[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
#		]
#	Օգտագործել zip() function-ը այնպես որ ստանանք
#		[('Lilit', 1, 8, 15),
#		 ('Aren', 2, 9, 16),
#		 ('Janna', 3, 10, 17),
#		 ('Samvel (Sam)', 4, 11, 18),
#		 ('Gohar', 5, 12, 19),
#		 ('Armen', 6, 12, 20),
#		 ('Luiza', 7, 14, 21)]


users_list = [
				"Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
				[
                  [1,2,3,4,5,6,7],
                  [8,9,10,11,12,13,14],
                  [15,16,17,18,19,20,21]
                ]
]

x = zip(users_list[0:7], *users_list[7])

print(list(x))

