def say_hello(name):
    print(f"Hello, {name} world!")

say_hello("Nature")
say_hello("Crazy")
say_hello("miniature")

my_list = {"things", "dogs", "miniature"}
for i in my_list:
    say_hello(i)

def square(a): 
    return a ** 2

result = square(4)
print(result)

for i in range(1,result):
    print(i)

def square(number):
    return number
result = square(5)
print(help(result))

def calc_area(width, height):
    return width * height

result = calc_area(2, 5)
print(result)

def temp_message(temp):
    nmb = int(input("Give a number: "))
    if nmb <10:
        print("cold")
    elif nmb > 10 and nmb < 25:
        print("moderate")
    else:
        print("hot")

result = temp_message()  # Here we have a problem when compiling

# Returns the bigger of two numbers
def larger(num_1,num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2
print(larger(3, 8))# 8
print(larger(10, 4))#10

def parameter_default(name = None):
    print(f"hello, {name}")
parameter_default()
parameter_default("Nico")

def power(base, exponent = 2):
    return base + exponent
result = power(2)
result1 = power(2, 3)
print(result)
print(result1)

