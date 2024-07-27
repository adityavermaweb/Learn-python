str1 = "apna"
len1 = len(str1)
print(len1)


str2 = "college"
final_str = str1 + str2
print(final_str) 



#--------- Indesing ----------->

str = "apna college"
print(str[5])


#--------- Slicing ------------>

str = "apna college"
print(str[0:5])


#-------- Negative Index --------->

str = "apple"
print(str[-3: -1])



#----------  String Function  ----------->

str = "i am a coder"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("a", "aa"))
print(str.find("c"))
print(str.count("a"))



# Q-1) Write a program to input users first name & print its length ?

name = input("enter your name :")
print("length of your name is", len(name))

# Q-2) Write a program to find the occurrence of '$' in a String ?

str = "The money is $$$$"
print(str.count("$")) 



#-----------  Conditional Statements  -------------->

# if 
# elif

light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")    
else:
    print("light is broken")


marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student ->", grade)                           



# Q-1) Write a program to check if a number entered by the user is odd or even ?

num = int(input("enter a number : "))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")    



# Q-2) Write a program to find the greatest of 3 number entered by the user ?

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("A is greatest number", a)
elif(b >= c ):
        print("B is greatest number", b)
else:
      print("C is greatest number", c)        



# Q-3) Write a program to check if a number is a multiple of 7 or not ?

num = int(input("enter number :"))
if(num % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")    