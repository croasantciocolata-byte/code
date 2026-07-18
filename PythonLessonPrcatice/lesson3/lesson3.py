# Accessing characters in a string using indexing
hello = "hello"
print(hello[0])  # prints 'h'
print(hello[1])  # prints 'e'
print(hello[2])  # prints 'l'   
print(hello[3])  # prints 'l'
print(hello[4])  # prints 'o'
print()
print(hello[-5]) # prints 'h'
print(hello[-4]) # prints 'e'
print(hello[-3]) # prints 'l'
print(hello[-2]) # prints 'l'
print(hello[-1]) # prints 'o'
print("---------")

word = "Hello"
print(len(word))
print(word[len(word)-1]) # prints 'o'
word = "Hello", 123
print(len(word)) # prints 2 because there are two elements in the 
print("---------")
print()

word = "Hello"
print("third character is:", (word[len(word[2]) ])) # prints 'l'
print(word[len(word)-1]) # prints 'o'
print(len(word)) # 5
print(word[len(word)-2]) # prints 'l'
print("---------")

# Concatination
print(word[1] + word[2]) # prints 'el'
print("---------")

greeting ="hei there"
print(greeting)
print(len(greeting)) 
print(greeting[3]) # prints ' '
print("---------")

text = "strawberry"
print(text[0:5]) # straw
print(text[:5]) # straw
print(text[5:]) # berry
print(text[2:7]) # rawbe
print(text[2:2]) # blank space
print(text[1:-1]) # deletes s & y
print(text[-5:-1]) # berr
print(text[11:20]) # blank space


print("---------")
print(text.upper()) # STRAWBERRY
print(text.lower()) # strawberry

print("---------")
name = "sri lanka"
print(name.capitalize()) # Sri lanka

print("---------")
name = "banana"
print(name.count("a")) 

print("---------")
name = "cute"
cats = name.replace('c', 'h')
print("a.",cats) # hute
print("b.",name.replace('h', 'c'))

print("---------")
name = "cute"
print(name.replace("u", "a").replace("c", "h"))
word = 'experience'
print(word.count('e'))

print("---------")
listcheck = ["apple", "banana", "cherry", "orange", "kiwi"]
print(listcheck)
print(listcheck[1]) # banana
print(listcheck[-2:])

print(listcheck[1:3]) # banana, cherry
print(listcheck[:3]) # apple, banana, cherry
print("---------")


word = ["love", "live"]
word.append("laugh") #  insert the word at the end
print(word)

word.remove('live')
print(word)



# brake password
"""pas1: cate caractere are parola
pas2: cauti daca un anumit caracter e in password
pas3: daca e in parola, afisezi pozitia lui"""

