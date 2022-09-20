#Tutorial 3

x = int(input("Type the number "))
if x==1 or x==2:
    print("Positive")
elif x==-1 or x==-2:
    print("Negative")
else:
    exit()   # since the question dont say what to do else ...

i = int(input("Type the number "))
if i%2==0:
    print("Even number")
else:
    print("Odd number")

mark = int(input("What is your mark? "))
if mark < 0 or mark > 100:
    print("Invalid Mark")
elif mark >= 70:
    print("Exceptional result!")
elif mark >= 40:
    print("Satisfactory result!")
else:
    print("You have failed.")

mark = int(input("Enter the mark "))
if mark<25:
    print("F")
if 25<=mark<45:
    print("E")
if 45<=mark<50:
    print("D")
if 50<=mark<60:
    print("C")
if 60<=mark<80:
    print("B")
if 80<=mark:
    print("A")

value_1 = float(input('Enter the value 1 '))
operator = input('Select the operator +,-,*,/ ')
value_2 = float(input('Enter the value 2 '))
if operator == "+":
    print(int(value_1 + value_2))
elif operator == "-":
    print(int(value_1 - value_2))
elif operator == "*":
    print(int(value_1 * value_2))
elif operator == "/":
    if value_2 == 0 :
        print('Invalid')
    else:
        print(int(value_1 / value_2))
else :
    exit()

age1 = int(input("Enter the age of 1st person "))
age2 = int(input("Ënter the age of 2nd person "))
age3 = int(input("Enter the age of 3rd person "))

if age1 < (age2 and age3):
    print("1st person is youngest")
elif age2 < (age1 and age3):
    print("2nd person is youngest")
else:
    print("3rd person is youngest")
if age1 > (age2 and age3):
    print("1st person is oldest")
elif age2 > (age1 and age3):
    print("2nd person is oldest")
else:
    print("3rd person is oldest")

temp = float(input('Temperature of water? '))
if temp <= 0:
    print('Frozen')
elif temp <= 12:
    print('Cold')
elif temp <= 25:
    print('Warm')
elif temp <= 75:
    print('Hot')
elif temp <= 100:
    print('Very hot')
else:
    print('Burning')

x=10
y=20
z=30

if x==10:
    if y==20:
        print("End of nested if block")
    else:
        print("End of nested if-else block")
else:
    if y==20:
        print("Elif block")
    else:
        if z==30:
            print("End of nested if block")
        else:
            print("End of nested if-else block")