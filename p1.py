def p1():
    a = input("Enter a positive integer :")
    divisors = []
    for i in range(1,(a+1)6):
        if a%i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        print("There are only %s divisors so %s IS a prime number."% (divisors[0], divisors[1]))
    else:
        print('Divisors of %s are:'%(a) + str(divisors))
        print("There are %s divisors so %s is NOT a prime number." % (len(divisors), a))

p1()