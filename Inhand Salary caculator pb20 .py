'''
Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%),
and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
'''


salary = int(input("Enter your annual salary: "))

# calculate tax deduction
if salary>=1 and salary<=499999:
    tax = (0)*salary
    af_tax = salary-tax

elif salary>=500000 and salary<=1000000:
    tax = (10/100)*salary
    af_tax = salary - tax

elif salary>=1000001 and salary<=2000000:
    tax = (20/100)*salary
    af_tax =salary-tax

else:
    tax = (30/100)*salary
    af_tax = salary-tax

# calculate Hra, da, pf tax deduction
hra = (10/100)*af_tax
da = (5/100)*af_tax
pf = (3/100)*af_tax
print(f"After reduction salary is {af_tax})")

in_hand_salary = (af_tax-hra-da-pf)/12
print(f"Inhand salary is {in_hand_salary}")


if in_hand_salary<=999:
    print(in_hand_salary)

elif in_hand_salary>=1000 and in_hand_salary<=9999:
    print(f"Inhand salary is '{in_hand_salary/1000}k'")

elif in_hand_salary>=100000 and in_hand_salary<=9999999:
    print(f"Inhand salary is '{in_hand_salary/1000000}L'")

else:
    print(f"Inhand salary is '{in_hand_salary/10000000}Cr'")


