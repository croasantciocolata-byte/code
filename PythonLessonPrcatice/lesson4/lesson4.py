my_tuple = ("Python", "Java", "C++")
print(my_tuple[0])

tr = (8,2,7,4,5,3,9)
print(tr.index(4)) # arata indexul lui 4 (4 e in index 3 - gen...0 1 2 3)
print("----")
print(tr.count(2)) # arata cate de 2 sunt in lista

my_tuple = ("Python", "Java", "C++")
print(my_tuple.index("C++")) # arata indexul lui C++ (C++ e in index 2 - gen...0 1 2)
print("----")
print(my_tuple.count("C++")) # numara cate de C++ sunt in liste

t = (1, [2, 3], 4)
t[1][0] = 99
print(t)

t = ("blue", "green", "red")
a, b, c = t
print(c)

num = 1, 2, 3
number = num
print(number)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
print(t1 * 3) # prints tuple 3 times

t = (10, 20, (30, 34), 40, 50)
print(t[2:])
print("----")


# Dictionary Key => value
student ={
    "name": "Nico",
    "age": 25,
    "grade": "A"
}
print(student["name"])

student["grade"] = "A+"
print(student["grade"])

print(student)

student["booksBought"] = 5
print(student)

print(student.get("school"))

student.update({"age": 26})
student["grade"] = "A++"
student.update({"school": "MIT"})
print(student)

student.pop("booksBought") #sterge booksBought
print(student)

del student["age"] #sterge age
print(student)

key = student.keys() #arata keyle adica name, age, grade, etc
value = student
print(key)
print(value)    


print("----")

elev = {
    "book" : {
        "name":  "Aphrodite",
        "age" : 20,
        "grade": "A"
    }
}
print(elev["book"]["age"])
print("----")

# Sets - sorting, no duplicates
numbers = 1, 2, 3, 4, 1, 3,5 
print(numbers)
num = {2, 1, 3, 4, 1, 3, 5} # no duplicates}
print(num)
print("----")

fruits = {"apple", "banana", "cherry"}
print(fruits)

my_set = set()
print(my_set)
my_list = list()
print(my_list)
my_list.append("asds")
print(my_list)
print("----")

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "kiwi", "banana"}
print(fruits | fruits2) # all items from both a and b - apple, banana, cherry, orange, kiwi
print(fruits & fruits2) # what is in both a and b - banana
print(fruits - fruits2) # what is in a but not in b - apple, cherry
print(fruits ^ fruits2) # what is only in a and only in b - apple, orange, kiwi, cherry
print("-----")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("cherry")
print(fruits) # removes cherry if exists, if not, does nothing
print("----")

a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b)) # returns a set that contains all items from both sets, duplicates are excluded

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b)) # returns a set that contains only the items that are present in both sets
print(a.difference(b)) # returns a set that contains the items that are present in the first set but not in the second