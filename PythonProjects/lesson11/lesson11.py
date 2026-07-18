# class Student:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Student name: {self.name}, Age: {self.age}"
#     def introduce(self):
#         return f"Hi , I'm {self.name} and i'm {self.age} years old"
#     def what_do(self):
#         return f"I'm {self.name}"
    
# # student = Student("Alice" , 14)
# # print(student.introduce())
# # student =  Student("Alice", 12) 
# # print(student.name)
# # print(student.age)
# # print(student)

# # Add a new attribute called subject to the class. This attribute should store the student’s 
# # favourite subject in school.
# # What You Need to Do:
# # Modify the __init__ method to accept a third parameter: subject.
# # Store it using self.subject.
# # # Update the __str__ method so it also shows the subject.
# # student = Student("Alice", 23, "video")
# # print(student.introduce())
# # print(student)

# # Add a method called study to the class.
# #  This method should return a sentence that shows what subject the student is studying.
# student = Student("Mihail",29)
# print(id(student))
# # del student.name

# print(hasattr(student, "age"))
# print(getattr(student, "age"))
# print(getattr(student, "sub","asdasd"))
# setattr(student, 'club', "Vlad")
# print(setattr(student, "age" , "32"))
# print(student)
# print(student.club)
# print(vars(student))

# class Laptop:
#     def __init__(self, brand):
#         self.brand = brand

# l = Laptop("Dell")
# print(hasattr(l, "brand"))
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"My name is {self.name}"
#     def greet(self):
#         return f"Hello, my name is {self.name}"
# class Student(Person):
#     def __str__(self):
#         return f"{self.name} is studing"
#     def study(self):
#         return f"{self.name} is studing"
    
# student = Student("Mihail")
# student1 = Person("Miha")
# print(student1)
# print(student)
# print(student.greet())
# print(student.study())

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"My name is {self.name}"
#     def greet(self):
#         return f"Hello, my name is {self.name}"
# class Student(Person):
#     pass

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"{self.name}"

# class Student(Person):
#     def __init__(self,name, subject):
#         self.subject = subject
#         self.name = name
#     def __str__(self):
#         return f"{self.name} {self.subject}"

# student1 = Person("Vasea")
# print(student1)
# student = Student("Mihjai" , 29)
# print(student)


# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"{self.name}"

# class Student(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def __str__(self):
#         return f"{self.name} {self.subject}"

    
# student = Student("Mihjai" , 29)
# print(student)


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     pass

# dog1 = Dog("Buddy")
# print(dog1.name)

# class A:
#     def __init__(self):
#         self.value = 5

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.value += 10

# b = B()
# print(b.value)
