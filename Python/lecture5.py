# -------- While Loop -------->

# To print numbers from 1 to 10 by using while loop

x = 1
while x <= 10:
    print(x)
    x += 1

# To display the sum of first n numbers

n = int(input("Enter number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
    print("The sum of first",n, "number is : ",sum)

# LET's PRACTICE


# Q.1) Print numbers from 1 to 100.

n = 1
while n <= 100:
    print(n)
    n += 1 


# Q.2) Print numbers from 100 to 1.

i = 100
while i >= 1:
    print(i)
    i -= 1


# Q.3 Print the multiplication table of a number n.

n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


# Q.4) Print the elements of the following list using a loop:
        # [1, 4, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# Q.5) Search for a number 'x' in this tuple using loop:
        # (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i) 
        break
    i += 1  
