def gcd(a, b):
    c = a
    d = b
    while True :
        if a == b:
            print('''GCD is found and it is %s \nLCD is found and it is''' % a, int(c*d/a))
            break
        elif a > b:
            a = a-b
        else:
            b = b-a

gcd(60,35)