name = "Aditya Verma"
age = 22
salary = 70000.25

print(type(name))
print(type(age))
print(type(salary))

# Sum of two numbers

a = 10;
b = 10;
sum = a + b;
print(sum); 


# -------------  Arithmetic Operators  ---------------

a = 4
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)


# -----------   Relational Operators  ---------------

a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a < b) #False
print(a >= b) #True
print(a <= b) #False


# ----------  Type Conversion  ---------------

a = 2
b = 4.25

sum = a + b
print(sum)

# ---------  Type casting  -------------

a, b = 1, "2"
c = int(b)
sum = a + c
print(sum)



 # Q-1) Write a Program to input 2 numbers & print their sum.

first_number = int(input("enter the first number: "))
second_number = int(input("enter the second number: "))

print("sum = ", first_number + second_number)



# Q-2) Write a Program to input side of a square & print its area.

side = float(input("side of the square : "))
print(side * side)



# Q-3) Write a Program to input 2 floating point numbers & print their average

a = float(input("enter first :"))
b = float(input("enter second :"))

print("avg = ", (a + b)/2)



# Q-4) Write a program to input 2 int numbers, a and b.
#    Print True if a is grater than or equal to b. If not print False.

a = int(input("enter first :"))
b = int(input("enter second"))

print(a >= b)