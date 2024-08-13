# --------------------Function & Recursion---------------------->
# Eg 1: Write a function to print Hello ?

def wish ():
    print("Hello Good Morning")
wish() 
wish()   


# Eg 2: Write a function to take name of the student as input and print wish messages by name.

def wish(name):
    print("Hello",name,"Good Morning")
wish("Aditya")
wish("Durga")  


# Eg 3: Write a function to take number as input and print its square value.

def squareIt(number):
    print("The Square of",number,"is",number*number)
squareIt(4)
squareIt(5)
squareIt(2)  


# Eg 4: Write a function of calculate average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(98, 97, 95)


# Eg 5: Write a function to print the length of a list.(list is the parameter).

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor","iranman","captain america","shaktiman"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)