#Tutorial 5

for i in range(1,100):
    #outer loop iterates 1 to 99
    for j in range(1,50):
        #inner loop iterates 1 to 49
        print(str(i)+" "+str(j))

import random
counter=0
for i in range(50):
    dice_1=random.randint(1,6) #randint --> the (1,6) means including 6
    dice_2=random.randint(1,6)
    if (dice_1==dice_2):
        counter+=1
print('Out of 50 you rolled', counter, 'doubles')


num = int(input('Enter the number: '))
for num in range(1, num+1):
    print(num**3)
    num += 1

for y in range(5,0,-1):
    for x in range (y):
        print('5', end="")
    print("")

for i in range(5, 0, -1):
    print('5' * i)

row = 7
for i in range(row):
    for s in range(row, i, -1):
        print(end=" ")
    for j in range(i+1):
        print(end="* ")
    print()
#
s=15
for i in range(1,8):
    print(''
          ''*s,end=' ')
    print('*'*i)
    s-=1


space=8   # Try as the above way
for i in range(5):
    for j in range(space):
        print(" ", end="")
    space-=2
    for j in range(i+1):
        print(" *", end="")
    print()

space=4
for i in range(1,6):
    print(" "*space, "*"*(5-space))
    space-=1


6
num = int(input('Enter the number: '))
fac = 1
for i in range(1, num+1):
    fac*=i
print(fac)

import random
num = random.randint(0,10)
guesses_left = 3

while guesses_left>0:
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You loss")


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
  total_score = 0
  for c in word:
    for item in score:
      if c.lower() == item:
        total_score += score[item]
  return f"Your score is {total_score}"

your_word = input("Enter your word here: ")
print(scrabble_score(your_word))