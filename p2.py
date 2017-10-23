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