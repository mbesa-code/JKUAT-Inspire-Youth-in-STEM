# variables in python
student_name="john"#string
student_second_name="doe"#string
student_age=17#integer
student_height=1.51#float
student_admitted=True#boolean

# operation in python
#1. arithmetic operators
num1=10
num2=20
additon=num1+num2
# print(addition)
subtruction=num2-num1
# print(subtruction)
num1<num2

#2. comperison operators
print(num1==num2)#False
print(num1!=num2)#True
print(num1>num2)#false
print(num1<num2)#True

#3. logical operators
print(num1<num2 and num1>num2)#false
print(num1<num2 or num1<num2)#True
print( not num1<num2)#false

#4. assignment operators
# =, +=, -=, *=, /=
# num1 +=5
# print(num1)#15
# num1 -=5
# print(num1)#10
# num1 *=5
# print(num1)#50

#5. identity operators
# is, is not
# prrint(num1 is not num2)#True
# print(num1 is num2)#false

#6. conditional statements
# if, elif, else

if student_age >= 18:
    print("you are an adult")
enter_name = input("enter your name:")
enter_age = int(input("enter your age: "))
if enter_age >= 18:
    print(enter_name,"is an adult") 
else:
    print
