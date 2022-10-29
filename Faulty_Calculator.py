# Faulty Calculator
#Faults need to create to avoid cheating
#45*3=555,56+9=77, 56/6=4

print("Welcome to our calculator")
print("Enter your frist number")
num1 = int(input())
print("Enter your calculation sign\n"
      "for add type +\n"
      "for subtraction type -\n"
      "for multiply type *\n"
      "for division type /\n")
a = "+"
s = "-"
m = "*"
d = "/"
cal = input()
print("Enter your second number")
num2 = int(input())
if cal==a:
    if num1==56 and num2==9:
        print(77)
    else:
        print(num1 + num2)
elif cal==s:
    print(num1 - num2)
elif cal==m:
    if num1==45 and num2==3:
        print(555)
    else:
        print(num1 * num2)
elif cal==d:
    if num1==56 and num2==6:
        print(4)
    else:
        print(num1/num2)
else:
    print("Wrong Input")
