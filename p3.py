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