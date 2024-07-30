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