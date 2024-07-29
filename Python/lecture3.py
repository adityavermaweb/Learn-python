# ---------List & Tuple in Python --------------->
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(len(marks))

# --------------List Slicing------------------>

list = [85, 94, 76, 63, 48]
print(list[1:4])

# -------------List Methods------------------->

list = [2, 1, 3]
list.append(4)
list.sort()
list.sort( reverse = True)
list.reverse()
list.insert(3,4)
list.remove(1)
list.pop(0)
print(list) 


# -------------Tuples in Python---------------->

tup = (2, 1, 3, 1)
print(tup.index(3))
print(tup.count(1))


# Q-1) Write a program to ask the user to enter names of their 3 favorite movies & store them in a list ?

movies = []
mov1 = input("enter 1st movies: ")
mov2 = input("enter 2nd movies: ")
mov3 = input("enter 3rd movies: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)


# Q-2) Write a program to check if a list contains a palindrome of elements.(Hint: use copy() method) ?

list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")



# Q-3) Write a program to count the number of students with the "A" grade in the following tuple ?

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


# Q) Store the above value in a list & sort them from "A" to "B" ?

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)