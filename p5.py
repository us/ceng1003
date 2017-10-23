def p5():
    while True:
        a = int(input("Enter withdrawal amount : "))
        if 9 >= a >=55:
            break
        else:
            print("Oops!  Number is must be between 5 and 9. Try again...")
            a = input("Enter withdrawal amount : ")


# pattern1
def pattern1(a):
    for i in range(a+1):
        print(i*str(i))

# pattern2
def pattern2(a):
    for i in range(1,a+1):
        print((a-i) * '.' + i*str(i))

# pattern3
def pattern3(a):
    for i in range(1, a + 1):
        if i%2 != 0:
            for j in reversed(range(1, i+1)):
                print(j, end = '')
            print('')
        else:
            print(i*str(i))

# pattern4
def pattern4(a):
    print('*')
    for i in range(a+1):
        print('*' + i*'-'+'*')
    print((a+3)*'*')

# pattern5
def pattern5(a):
    for i in range(1,a+1):
        arr = []
        for j in range(1, (a + 1)):
            arr.append(0)
        arr[i-1] = i
        arr[-i] = i
        print(arr)

# pattern6
def pattern6(a):
    for i in reversed(range(1,a+1)):
        print((a-i)*' ' + str(i), end = '')
        print((i-1)*('-' + str(i)))

# pattern7
def pattern7(a):
    print(a*'+')
    for i in range(1,a-2):
        print('+' +((a-2)*'*') +'+')
    print(a*'+')


# pattern8
def pattern8(a):
    for i in range(1, 4):
        if i == 1 or i == 3:
            for j in range(1, a+1):
                if j%2 != 0:
                    j = '+'
                else:
                    j = '-'
                print(j, end='')
            print('')
        else:
            for k in range(2, a):
                if k % 2 != 0:
                    k = '+'
                else:
                    k = '-'
                print(k + (a - 2) * '*' + k)

