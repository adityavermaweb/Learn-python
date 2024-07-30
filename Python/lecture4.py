#------------------ Dictionary in Python ----------------->

info = {
    "key" : "value",
    "name" : "Aditya",
    "learning" : "Python"
}
print(info["name"])


# ---------------- Nested Dictionaries --------------->

student = {
    "name" : "Aditya",
    "score" : {
        "python" : 92,
        "javaScript" : 89,
        "css" : 95
    }
}
print(student["score"]["python"])

# ----------------- Dictionary Methods --------------->

student = {
    "name" : "Aditya",
    "score" : {
        "python" : 92,
        "javaScript" : 89,
        "css" : 95
    }
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

new_dict = {"name" : "Ayush", "age" : 20}
student.update(new_dict)
print(student)




# ----------------Set in Python ---------------->

collection = {1, 2, 3, 4, "hello", "world"}

print(collection)
print(type(collection))


# Create a empty set syntax -->

collection = set() #empty set: syntax

print(type(collection))

# -------------- Set Methods ------------->

collection = set()
collection.add(1)

print(collection)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1.intersection(set2))


# ----Practice Question-----

# Q-1) Store following word meanings in a pyth6on dictionary :
    # table : "a piece of furniture", "list of facts & figures"
    #  cat : "a small animal"

# Sol
dictionary = {
    "cat" : "A small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)



# Q-2) You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++","python", "javascript", "java", "python","java", "C++", "C"

# Sol

subjects = {
    "python", "java", "C++", "python", "javascript", "java",
    "pyhton", "java", "C++", "C"
}

print(subjects)



# Q -3) Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# Sol

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)



# Q-4) Figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built- in data types)

# Sol

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)

