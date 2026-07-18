def word_count(text):
    return len(text.split())

def word_count(text):
    return len(text.split())

def is_palindrom(text):
    word = text.lower().replace(" ", "")
    return word == word[::-1]

def capitalise_sentences(text):
    sentences = text.split(". ")
    capital = [s.strip().capitalize() for s in sentences]
    return ". ".join(capital)

def count_vowels(text):
    vowel = "AaEIBosuAOOo"
    count = 0
    for v in vowel:
        for i in text:
            if v == i:
                # return True
                count+=1
    # return False
    return count

get_function = input("From function choice: word_count, is_palindrom, capitalise_sentences, count_vowels: ")
if "word_count" == get_function:
    sample_text = "Hello world! This is a sample text."
    count = word_count(sample_text)
    print(count)
elif "capitalise_sentences" == get_function:
    word = "radar"
    get_bool = capitalise_sentences(word)
    print(get_bool)
elif "is_palindrom" == get_function:
    word = "radar"
    get_bool = is_palindrom(word)
    print(get_bool)
elif "count_vowels" == get_function:
    word = "radar"
    get_bool = count_vowels(word)
    print(get_bool)
else:
    print("choose")

while True:
    command = "Type 0 to exit program:"
    if command == '0':
        break
    print("This will repeat")
    print("1. word_count")
    print("2. is_palindrom")
    print("3. capitalise_sentences")    
    print("4. count_vowels")
    print("0. exit")

    choice = input("Enter your choice: ")
    print(f"You chose: {choice}")

    if choice == '1':
        text = input("Enter text: ")
        result = is_palindrom(text)
        print(f"Word count: {result}")
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")