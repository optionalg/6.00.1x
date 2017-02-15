'''for i in range(2,12,2):
    print(i)
print('Goodbye!')
'''

'''print('Hello!')
for i in range(0, 10, 2):
    print(10-i)
'''

'''end = 6
total = 0

for i in range(1, end+1):
    total+=i
print(total)
'''

'''num = 10
for num in range(5):
    print(num)
print(num)
'''

'''divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)
'''

'''for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
'''

'''greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
'''

'''school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
'''

'''iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
'''

'''s = 'azcbobobegghakl'
num_of_vowels = 0
for letter in s:
    if letter in 'aeiou':
        num_of_vowels += 1
print('Number of vowels: ' + str(num_of_vowels))
'''

s = 'tltblray'
longest = ''
sequence = ''
current = ''
broke = 0

for letter in s:
    if letter >= current:
        sequence += letter
        print(letter)
    else:
        if len(sequence) > len(longest):
            longest = sequence
        sequence = letter
        print('-')
    current = letter

if len(sequence) > len(longest):
    longest = sequence


print('Longest substring in alphabetical order is: ' + str(longest))
