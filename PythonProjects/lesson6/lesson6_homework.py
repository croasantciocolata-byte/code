favourite_colour = input("Enter your favourite colour: ")
number = input("Enter a number between 1 and 5: ")
print()

favourite_colour = favourite_colour.strip().lower()
match favourite_colour:
    case "red":
        print("Did you know people who like red are seen as leaders?")
    case "blue":
        print("Did you know people who like blue are seen as calm and trustworthy?")
    case "green":
        print("Did you know people who like green are seen as balanced and nature-loving?")
    case _:
        print("That's an interesting choice of colour!")
print()

if int(number) == 1:
    print("Cool!")
elif int(number) == 2:
    print("Nice!")
elif int(number) == 5:
    print("That's actually my favourite number!")
else:
    print("Hmmm")
print()

if favourite_colour == "blue" and int(number) == 3:
    print("Something special !!!")
