def prime_checker(number):
    is_prime = True

    # cycle through values from 2 - number
    for i in range(2, number):
        # if number is divisible by i then not prime
        if number % i == 0:
            # number can't be prime if divisible by any value in range
            is_prime = False

    if is_prime:
        print("It's a prime number!\n")

    else:
        print("It's not a prime number\n")


n = int(input("\nPlease input a number to check if it's a prime number: "))
prime_checker(number=n)