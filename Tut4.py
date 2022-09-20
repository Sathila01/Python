#Tutorial 4

number = int(input('Enter the number: '))
cycle = int(input('Enter number of cycles you want: '))
count = 1
while count <= cycle:
    output = count*number
    count += 1
    print(output)


num = 0
sum = 0
while num != -1:
    num = int(input('Enter the number: '))
    sum = sum + num
print('Total is '+str(sum))

hidden_num = 21
score = 100

while score != 0:
    guessed_num = int(input('Enter your guess here: '))
    if guessed_num == hidden_num:
        print('You won!')
        break
    score -= 5
if score == 0:
    print('No more attempts')

import random

hidden_num = random.randint(1,100)
score = 100

while score != 0:
    guessed_num = int(input('Enter your guess here: '))
    if guessed_num == hidden_num:
        print('You won!')
        break
    score -= 5
if score == 0:
    print('No more attempts')


row = 1
while row <= 6:
    col = 1
    while col <= row:
        print(col, end="")
        col +=1
    row += 1
    print('')

row = ''
num = 1
while num <= 6:
    row += str(num)
    print(row)
    num += 1

counter = 1
while counter != 100:
    print(counter)
    counter += 1

import random as rand
var=10
gen_num=rand.randint(1,1515151515)
while gen_num != 2:
      print('Random num is not 2')
      gen_num = rand.randint(1, 1515151515)
else:
     print('Finally it is 2')

count = 1
while count <= 3:
    p = int(input('Enter 1st number: '))
    n = int(input('Enter 2nd number: '))
    r = int(input('Enter 3rd number: '))
    si = p*n*r / 100
    print(si)
    count += 1
else:
    exit()

for i in range(9,-1,-1):
    if i==5:
        break
    print('Current value:', str(i))

for i in range(9, -1, -1):
    if i==5:
        continue
    print('Current value:', str(i))
else:
    print('bye!')