# Task 1. Ինչ type կվերադարցնի հետեվյալ արտահայտությունը ու ինչ պատճառով ` 1 + 2.0 +3
# 6 qani vor float enq ogtagorcum.

# Task2 2. Ունենք հետեվյալ արտահայտությունը` 2 * 3 + 4.Ինչպես կարանք փոխենք արտահայտությունը այնպես որ առաջինը գումարի հետո նոր բազմապատկի   
#   2 * (3 + 4) 

# Task 3. Ինչպես կարանք կլորացնենք 2.555 որ ստանանք 2.56 
print(round(2.555,2))

# Task 4. Ունենք 2 բառից կազմված ինչ որ string օրինակ `'Hello world':
#    Օգտագործելով string-ի մեթոդներից պետքա ստանալ տեքստի հակառակ ձեվը - "world Hello"

str = 'Hello World'
space_index = str.find(' ')
print(str[space_index + 1:] + ' ' + str[0:space_index])

# Task 5. Գնացեք այս հղումով (https://www.lipsum.com/) ու այնտեղ առաջին տեքստում կտեսնեք մոտավորապես սենց տեքստ
#     s1 = 'Lorem Ipsum is  ...  dummy text of the printing and typesetting industry.
#	   Lorem Ipsum has been the industry's standard dummy text ever since the ...s,
#	   when an unknown printer took a ...  of type and scrambled it to make a type
#	   specimen book'.
#    Օգտվելով առաջին տեքստից լրացրեք բառերը օգտագործելով string-ի format()-ի 3 գործիքները 
#    1. "" % ()
#    2. .format
#    3. f""

word1, word2, word3 = 'simple', 1500, 'galley'

s1 = "Lorem Ipsum is %s dummy text of the printing and typesetting industry.Lorem Ipsum has been \n the industry's standard dummy text ever since the %ds, when an unknown printer took a \n %s of type and scrambled it to make a type specimen book." % (word1, word2, word3)

s2 = "Lorem Ipsum is {0} dummy text of the printing and typesetting industry.Lorem Ipsum has been \n the industry's standard dummy text ever since the {1}s, when an unknown printer took a \n {2} of type and scrambled it to make a type specimen book.".format(word1, word2, word3)

s3 = f"Lorem Ipsum is {word1} dummy text of the printing and typesetting industry.Lorem Ipsum has been \n the industry's standard dummy text ever since the {word2}s, when an unknown printer took a \n {word3} of type and scrambled it to make a type specimen book."

print(s3 == s2 == s1)

# Task  6. Ունենք սովորական int type-ի թիվ օրինակ` 97
#    Ինչպես կարող ենք ստանալ առանձին 7-ը հետո 9-ը օգտագործելով միայն օպերատորներ եվ թվեր (string # չդարձնեք, եղավ՞ ։)


num = 97

print(num % 10, num // 10)

# Task 7.  Ունենք սովորական int type-ի թիվ օրինակ` 123 
#    Պետքա բոլոր թվերի գումարը ստանանք 6 օգտագործելով միայն օպերատորներ եվ թվեր (նորից, string չդարձնեք :) )

num2 = 123
sum = 0

last_digit = num2 % 10
sum += last_digit
num2 = num2 // 10

last_digit = num2 % 10
sum += last_digit
num2 = num2 // 10

sum += num2

print(sum)


# 1. Փորձեք գտնել թե ոնց կարանք վերցնենք միանգամից մեր string-ի վերջին տառը:

print(str[len(str) - 1])
print(str[-1])

# 2. Փորձեք հասկանալ ինչ է անում strip() մեթոդը:

# It removes whitespaces.

# 3. Փորձեք հասկանալ ինչ են անում """-ը, օրինակ """some long text"""

# It is for keeping string lines or tabs or create string whithin will be text like that "Some text".



