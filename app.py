'''
num1 = int(input("Enter the first number: "))
action = input("Enter desired action: ")
num2 = int(input("Enter the second number: "))

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == ":" or action == "/":
    print(num1/num2)
else:
    print(num1*num2)

x = 2
print (x == 2)'''

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)