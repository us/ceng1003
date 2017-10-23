def p1():
    a = input("Enter a positive integer :")
    divisors = []
    for i in range(1,a+1):
        if a%i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        print("There are only %s divisors so %s IS a prime number."% (divisors[0], divisors[1]))
    else:
        print('Divisors of %s are:'%(a) + str(divisors))
        print("There are %s divisors so %s is NOT a prime number." % (len(divisors), a))

#p1()

def p2():
    c = input("Enter withdrawal amount : ")
    a = c
    mny = [100, 50, 10, 5, 1]
    out = []
    for i in (mny):
        b = a / i
        if  b > 0:
            a = a-i*b
            out.append('%sx%sTL'%(b, i))
    print("%sTL = " % c + ' + '.join(out))

#p2()

def p3():
    arr = []
    a = arr.append(input("Number please: "))
    while arr[-1] > 0:
        a = arr.append(input("Number please: "))

    arr.pop()
    #print(arr)
    total = 0
    for i in (arr):
        total = total + i
    print("Total : " + str(total))
    print("Average: " + str(float(total)/float(len(arr))))

#p3()

def findMax(nums):
    result = nums[0] # assume first number is the maximum one
    max2 = nums[1]
    for num in nums[1:]: # check the rest of the numbers
        if num > result:
            result = num # if you find a larger num than the return result # current one found, modify your result
    print(result)

#findMax([4,6,1,7,8,9])

arr = [4,6,1,7,8,9,61,251,2351,523,5,5,600,500,700]
def findMax2(arr):
    max1 = arr[1]
    max2 = arr[2]

    for i in arr[2:]:
        if i > max2:
            if i >= max1:
                max2 = max1
                max1 = i
            else:
                max2 = i

    print(max2)


findMax2(arr)



