#q1

string = 'Monty Python'

print((string[0]))
print((string[11]))  # alternative string[-1]

print((string[len(string)-1]))
print((string[0:5]))

#q2
string = 'homebody'

print((string[:4]))  # alternative [0:4]

print((string[4:]))  # alternative [4:8]

#q3
stringS = eval(input("Enter a string with even length: "))

X = len(stringS)//2

print((stringS[0:X]))

print((stringS[X:]))

#q4
stringS = eval(input("Enter a string with odd length: "))

X = len(stringS)//2
Y = X + 1
print((stringS[X]))
print((stringS[:X]))
print((stringS[Y:]))  # alternative [X+1:]

#q7
x = 'acegikmoqsuwy'
y = 'bdfhjlnprtvxz'
z = ''

for i in range(len(x)):
    z = z + x[i] + y[i]

print(z)

#q10

S = 'I had a cat named amanda when I was little.'
count = 0
i = 0
while i < len(S):
    if S[i] == 'a':
        count += 1
    i += 1
print(count)

#q11
string1 = 'Spam, '
string2 = 'baked beans, '
string3 = 'Spam.'

menu = string1*5 + string2 + string1*4 + string3

print(menu)

#q13
print("I like writing in Python. \nIt is so much fun.")


#q18
my_string = input("Enter a string: ")
new_string = my_string.lower()

print(new_string)

#q19
some_string = 'NEW YORK'
new_string = some_string.title()

print(new_string)

#q23
name_str = "Albert Einstein"
first = name_str[:6]
last =  name_str[7:]
print(first, last)

# alternative 1
first = name_str[:name_str.find(' ')]
last  = name_str[name_str.find(' ')+1:]

print(first, last)

# alternative 2
first = name_str.split()[0]
last  = name_str.split()[1]

print(first, last)

#q24
brit_word = 'flavour'

amer_word = brit_word[:5] + brit_word[6:]

print(amer_word)

# alternative
amer_word = brit_word.replace('u','')

print(amer_word)

#q26
s = "Alan Turing"
print(s[::-1])

#q27
ab_string = 'abababababab'
a_string = ab_string[::2]

print(a_string)

#q28
string = 'abcdefghij'

string1 = string[::-1]
print(string1)

string2 = string[0::3]
print(string2)

string3 = string[-2::-2]
print(string3)

#q29
string = "Who's on first?"

print("o found at index:")
print(string.find('o'), end=' ')
print(string.find('o', string.find('o') +1))

#q30
name = 'Chapman , Graham Arthur'
last, comma, first, middle = name.split()

transformed = first + ' ' + middle + ' ' + last

print(transformed)



             
