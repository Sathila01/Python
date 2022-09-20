#Tutorial 6

try:
	print("I am trying to do something")
	raise TypeError("Type error has raised")  # now there's a type error
except TypeError:
	print("Type error captured")              # therefore this statement prints
else:
	print("Type error was not captured")
finally:
	print("This always executes")
#
#
try:
    print("I am trying to do something")
except TypeError:
    print("Type error captured")
else:
    print("Type error was not captured")
finally:
    print("This always executes")

x=1
assert x==2 #Assertion error
try:
	print(50/0)
except ArithmeticError as e:
	print(e)

try:
	int("Hello")
except ValueError as e:
	print(e)

try:
	100/0
except ArithmeticError:
	print("Arith")
except ZeroDivisionError:
	print("zero")

try:
	0.0000000001**100000000
except OverflowError as e:
	print(e)

#***************************
while True:
    n = input("Please enter an integer: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Requires a valid integer! Please try again.")
print("You successfully entered an integer.")

try:
    number = int(input("Enter the number: "))
    if number > 1000 :
        raise Exception('InputTooLarge')
    if number < 50 :
        raise Exception('InputTooSmall')
except Exception as e:
    print(e)

while True:
    user_input = input("Enter the formula:\n")
    formula = user_input.split()
    if len(formula) != 3:
        raise Exception('FormulaError')
    try:
        value1 = float(formula[0])
        value2 = float(formula[2])
        if not formula[1] == '+' or formula[1] == '-':
            raise Exception('FormulaError')
        else:
            if formula[1] == '+':
                print('The answer is: ', value1+value2)
    except ValueError:
        raise Exception('FormulaError')
    if user_input == 'Quit':
        break

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

try:
    total_likes = 0

    for post in blog_posts:
         total_likes = total_likes + post['Likes']

except KeyError:
    print("Check the dictionary again")

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

try:
    for x in food:
        fifth.append(x[4])

except IndexError:
    print('Check the list again')