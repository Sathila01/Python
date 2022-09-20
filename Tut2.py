#Tutorial 2

number_1 = int(input('1st number ')) #should put int to convert to integer; because by default input is a string
number_2 = int(input('2nd number '))
print(number_1 * number_2)



num_1 = int(input('Enter the 1st number: '))
num_2 = int(input('Enter the 2nd number: '))
total = (num_1 + num_2)
print(total)

Cel = float(input('Celsius value '))
Fa = (Cel*(9/5)) + 32
print(Fa)


value =  12.4
print(value)
print(type(value)) #class float

value=12
print(value)
print(type(value)) #class int ; type of the variable has changed

value = 20
print('The value is ' + str(value)) #str conversion should take place inside the print statement
print(type(value)) #value is still an int ; because we haven't covert it to a string explicitly

value=100
#print - version 1
print('value is ')
print(value)

#print - version 2
print('value is ', value)

#print - version 3 - To suppress printing of a new line, use end=' '
print('value is ', end=' ') #allows to add an additional horizontal line
print(value)

print("I'm a student \t")
print('This is a "great" website')
print("\nthe character to enter a new line")
print("This is a 'great' website")
print("test\ test2\ answers.txt")
print('\ is called a Backslash')

num = input("number: ")
if 0<int(num)<10 :

    print("Blue")
elif 10<int(num)<20 :
    print("Red")
elif 20<int(num)<30 :
    print("Green")
else :
    print("Not a correct color option")

num1 = "20"
num2 = "10"
print(num1 + num2)     #just adding those as strings
print(int(num1) + int(num2)) #they are converted to int ; so mathematical addition takes place

string= "abcde"
rstring= string[::-1]
print(rstring)