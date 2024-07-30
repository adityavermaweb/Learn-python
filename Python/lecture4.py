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
