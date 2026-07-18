# def def_Error(a, b):
#     assert b != 0, "Denominator must not be zero"
#     return a / b

# result = def_Error(5, 3)
# print(result)

# x = -1
# assert x >= 0, "x must be non-negative"

# print(10/ 0)


# age = -5
# assert age >= 0, "Age cannot be negative"13


# age = int(input("Enter your age: "))
# try:
#     if not age:
#         raise ValueError("ANot empty")
# except ValueError as ve:
#     print(ve)
# assert int(age) >= 0, "Age cannot be negative"
# assert int(age), "Not empty"

# def process_list(items):
#     assert isinstance(items, list), "Input must be a list"
#     assert all(isinstance(i, int) for i in items), "All items in the list must be integers"
#     assert len(items) > 0, "List must not be empty"

#     return [i * 2 for i in items]

# def multiply(a, b):
#     return a * b

# assert multiply(2, 3) == 6 
# assert multiply(3, 3) == 9   
# assert multiply(0, 10) == 0
# assert multiply(2, -4) == -8

# result = multiply(2, 3)
# print(result)  # Output: 6

# def is_even(n):
#     return n % 2 == 0

# assert is_even(4) == True
# assert is_even(6) == True

# def is_odd(n):
#     return n % 2 != 0

# assert is_odd(5) == True

# if __name__ == "__main__":
#     assert is_even(4) == True
#     assert is_odd(5) == True
#     print("All")

# import unittest

# class TestMath(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(2 + 3, 4)

#     def test_subtraction(self):
#         self.assertEqual(10 - 4, 6)

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# class TestCollection(unittest.TestCare):
#     def test_number_is_list(self):
#         numbers = [1, 2, 3, 4, 5]
#         self.assertIn(3, numbers)
#         # self.assertin(6, numbers)
#     def test_substring_in_string(self):
#         text = "Hello, world!"
#         self.assertIn("world", text)
#         self.assertIn("Python", text)

# if __name__ == "__main__":
#     unittest.main()
        
# import unittest
# class TestIdentity(unittest.TestCase):
#     def test_same_objects(self):
#         a = b = [1, 2, 3]
#         self.assertIs(a, b)
#         print(id(a), id(b))
#     def test_different_objects(self):
#         x = [1, 2, 3]
#         y = [1, 2, 3]
#         self.assertIs(x, y)
#         print(id(x), id(y))
    
# if __name__ == "__main__":
    # unittest.main()

# import unittest
# class TestType(unittest.TestCase):
#     def test_integer_type(self):
#         value = 10
#         self.assertIsInstance(value, int)

#     def test_string_type(self):
#         text = "Hello"
#         self.assertIsInstance(text, str)

#     # def test_list_type(self):
#     #     pi = 3.14   
#     #     self.assertIsInstance(pi, int)

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# class Animal:
#     pass
# class Dog(Animal):
#     pass
# class TestObjects(unittest.TestCase):
#     def test_dog_instance(self):
#         dog = Dog()
#         self.assertIsInstance(dog, Dog)
#         self.assertIsInstance

#     def test_wrong_instance(self):
#         number = 42
#         self.assertIsInstance(number, Dog)

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# class TestCondition(unittest.TestCase):
#     def test_math_condition(self):
#         self.assertTrue(5>3) #PASS

#     def test_string_condition(self):
#         word="Python"
#         self.assertTrue(len(word)==6) #PASS

#    def test_false_condition(self):
#         self.assertTrue(2+2==5) #FAIL   

# if __name__ == "__main__":
#     unittest.main()