#Task 1
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

for line_str in input_file:
    print(line_str, file=output_file)  # print to output_file
    next(input_file)

input_file.close()
output_file.close()


#Task 2
import string

wordFile = open('words.txt','r')

# collect all letters into a list
letters = []

for line in wordFile:
    for ch in line:
        if ch.lower() in string.ascii_lowercase: # only including lowercase implicitly igores punctuation
            letters.append(ch.lower())

# build a list of letter counts, implicitly in alphabetical order
letter_counts = []
for ch in string.ascii_lowercase:
    letter_counts.append(letters.count(ch))

# print histogram
for i in range(26):
    s = string.ascii_lowercase[i] + ': '
    for j in range(letter_counts[i]):
        s+= 'x'
    print(s)

#Task 3
    test_file = open('testFile.txt','r')
new_file = open('newFile.txt','w')

count = 0
s = ''
for line in test_file:
    line = line.split()
    for word in line:
        count += 1
        s += word
        if count%5 == 0: # every five words insert a carriage return
            s += '\n'
        else:
            s += ' '

new_file.write(s)
new_file.close()
test_file.close()

#Task 4
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()       # remove the carriage return
    for char in line_str:
        new_str = char + new_str      # concat at the left (reverse)
    print(new_str,file=output_file)   # print to output_file
    
input_file.close()
output_file.close()

#Task 5
s = input("Enter three integers (space separated): ")
a,b,c = s.split()

try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = a/b + c
except ValueError:
    print("Value Error:", a,b,c)
except ZeroDivisionError:
    print("Division by zero Error:", a, "/",b)


#Task 6
file_str = input("Open what file:")
find_line_str = input("Which line (integer):")

try:
    input_file = open(file_str) # potential user error
    find_line_int = int(find_line_str) # potential user error
    line_count_int = 1
    for line_str in input_file:
        if line_count_int == find_line_int:
            print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
            break
        else:
            line_count_int += 1
    else:
        print("Line {} of file {} not found".format(find_line_int, file_str))
        input_file.close()
except IOError:
	print("The file",file_str,"doesn't exist.")
except ValueError:
	print("Line",find_line_str,"isn't a legal line number.")

print("End of the program")