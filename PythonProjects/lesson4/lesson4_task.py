# Task 1
me = {
    "name": "Anastasia",
    "age": 17,
    "favouriteColour": "I've got no favourite colour"
}
print(me)
print("----")

#Task 2
me['pet'] = 'dog'
print(me)
print("----")

# Task 3
person = {
    "name" : "John",
    "age" : 30
}
person["hobby"] = "horse riding"
print(person)
print("----")

# Task 4
pupils = {
    "grade": "B"
}
print(pupils)
pupils.update({"grade":"A"})
print(pupils)
print("----")

# Task 5
Oameni = {
    "name": "Maria",
    "age": 22,
    "city": "Bucharest"
}
print(Oameni)
del Oameni["city"]
print(Oameni)
print("----")

# Task 6
familie = {
    "father": "John",
    "mother": "Jane",
    "sister": "Emily"
}
print(len(familie)) # prints how many keys are in dictionary
print("----")

# Task 7
book = {"title": "Python 101", "pages": 120}
print(book.get("lovbe"))
print("----")

# Task 8
school = {
    "subject": "Math",
    "teacher": "Mr. Smith",
    "room": 252
}
print(school)
print("----")

# Task 9
game = {"title": "Chess", "players": 2}
print(game.keys())
print(game.values())
print("----")

# Task 10
student = {
    "name": "Elena",
    "grades": {"Math": 8, "Science": 9}
}
print(student["grades"]["Science"])
print("-----")

# Task 11
inventory = {"apple", "banana", "apple", "cherry"}
print(inventory)






