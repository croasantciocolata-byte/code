#  Write a function called is_prime(n) that returns
#  True if n is a prime number and False otherwise.
def is_prime(n):
    if n <=1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0 and n > 2:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
#  Then, write at least five assert statements to
#  test your function with different inputs,
#  including:
#  A prime number
assert is_prime(3) == True, "This is not a prime number - change the number"
#  A non-prime number
assert is_prime(9) == True, "This is not a prime number - change the number"
#  The number 1
assert is_prime(1) == False,  "This is not a prime number - change the number"
#  A negative number
assert is_prime(-4) == False, "Prime numbers can not be negative"
#  The number 2
assert is_prime(2) == True, "This is not a prime number - change the number"
#  Make sure your assertions include descriptive
#  messages to indicate what each test checks