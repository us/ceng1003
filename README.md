[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# ceng1003 exercies

Following are some programming exercies. They aren’t in any difficulty order. Some of them are easy enough to be asked in the exam.

## Table of content
- [Exercies](#exercies)
    - [P1 (Prime Number)](#p1-prime-number)
    - [P2 (ATM)](#p2-atm)
    - [P3 (Total Average)](#p3-total-average)
    - [P3 (2) (findMax2)](#p3-2-findmax2)
    - [P4 (GCD)](#p4-gcd)
    - [P5 (Patterns)](#p5-patterns)
        - [Pattern 1](#pattern-1)
        - [Pattern 2](#pattern-2)
        - [Pattern 3](#pattern-3)
        - [Pattern 4](#pattern-4)
        - [Pattern 5](#pattern-5)
        - [Pattern 6](#pattern-6)
        - [Pattern 7](#pattern-7)
        - [Pattern 8](#pattern-8)
 - [Donation](#donation)
 - [Oh Thanks](#oh-thanks)



# Exercies

## P1 (Prime Number)
Read a positive integer number from the user and then display the numbers that divide this number without any remainder. Additionally, report how many such numbers are there and whether the input number is a prime number or not. Sample runs:

### Solution
```python
a = int(input("Enter a positive integer :"))
divisors = []
for i in range(1, a+1):
    if a%i == 0:
        divisors.append(i)

if len(divisors) == 2:
    print("There are only %s divisors so %s IS a prime number."% (divisors[0], divisors[1]))
else:
    print('Divisors of %s are:'%(a) + str(divisors))
    print("There are %s divisors so %s is NOT a prime number." % (len(divisors), a))
```

### Outputs
`Enter a positive integer : 0 The number should be positive.`<br>
`Enter a positive integer : 24`<br>

>>Divisors of 24 are : 1, 2, 3, 4, 6, 8, 12, 24 There are 8 divisors so 24 is NOT a prime number.<br>

`Enter a positive integer : 7`<br>

>>Divisors of 7 are : 1, 7<br>
There are only 2 divisors so 7 IS a prime number.<br>

## P2 (ATM)
Write a program that will determine how an ATM will give cash back to a user. Let’s assume that an ATM holds banknotes of type 100TL, 50TL, 10 TL, 5TL and 1TL. When the user enters the amount she wants to withdraw, the ATM tries to match this amount with the largest banknotes first. When the amount can’t be matched with just this type of banknote, it uses the next largest banknote and this continues until the whole amount is matched. Print how many of each banknote will be given back if the ATM utilizes this algorithm. See examples for more clarification:

### Solution
```python
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
```

### Outputs

`Enter withdrawal amount : 125 `<br>

>>125TL = 1x100TL + 2x10TL + 1x5TL

`Enter withdrawal amount : 873`<br>

>>882TL = 8x100TL + 1x50TL + 3x10TL + 2x1TL

`Enter withdrawal amount : 399`<br>

>>399TL = 3x100TL + 1x50TL + 4x10TL + 1x5TL + 4x1TL

## P3 (Total, Average)
Write a program that will read numbers from the user until the user enters a negative number. Then display the total and average of the numbers entered. Sample run:

### Solution
```python
arr = []
a = arr.append(input("Number please: "))

while arr[-1] > 0:
  a = arr.append(input("Number please: "))
arr.pop()

total = 0
for i in (arr):
    total = total + i
print("Total : " + str(total))
print("Average: " + str(float(total)/float(len(arr))))
```

### Outputs
`Number please: 12`<br>
`Number please: 6`<br>
`Number please: 15`<br>
`Number please: -2`<br>

>>Total : 33
Average : 11.0

## P3 (2) (findMax2)
Here is a function that will find the maximum value in a numbers list:
```python
def findMax(nums):
    result = nums[0] # assume first number is the maximum one
    for num in nums[1:]: # check the rest of the numbers
    if num > result: result = num # if you find a larger num than the return result # current one found, modify your result
```
Write a similar function called findMax2 that will return the second largest value inside its nums parameter. This is similar to finding the largest value but this time you have to keep track of the largest (i.e max1) and the second largest value (i.e max2) while you are iterating over the values in the array. Whenever you find a new array value that is larger then one of them you have to update these variables accordingly (i.e. if new value is larger than max1 then max2 becomes max1 and max1 becomes this new value, if it is only larger than max2 then only update max2 as this new value).
### Solution
```python
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
```

## P4 (GCD)
The following algorithm can be used to compute the greatest common divisor (GCD) of two numbers:
1. Read numbers A and B whose GCD will be computed<br>
2. If A equals B then GCD is A(orB)<br>
3. If A>B then make A equal to A-B, otherwise (if A < B) make B equal to B-A and then go back to step 2<br>

### Solution
```python
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
```

### Outputs
For instance, for values `A=60` and `B=35` the algorithm will work like this:<br>

![alt text](https://github.com/us/ceng1003/blob/master/exs.png "p4 outputs")

You can use a while loop containing some if-else statements to implement this algorithm. If GCD of two numbers are known, least common multiple (LCM) of these numbers can be computed by using the following equation:,`A*B = GCD(A,B)*LCM(A,B)`. Read two numbers from the user and then display their GCD and LCD by using the information above.
## P5 (Patterns)
Read a number from the user that is between 5 and 9 and then produce the following patterns. Hint: Use nested loops or duplicating a string by * operator: `“ab” * 5 -> “ababababab”`

### Solution
```python
while True:
    a = int(input("Enter withdrawal amount : "))
    if 9 >= a >=55:
        break
    else:
        print("Oops!  Number is must be between 5 and 9. Try again...")
        a = input("Enter withdrawal amount : ")
```
### Outputs
`Enter a number: 7`
##### Pattern 1:    
###### Solution
```python
for i in range(a+1):
    print(i*str(i))
```
###### Output  
```js
1  
22  
333  
4444  
55555  
666666  
7777777
```  
##### Pattern 2:
###### Solution
```python
for i in range(1,a+1):
    print((a-i) * '.' + i*str(i))
```
###### Output  
```js
......1  
.....22  
....333  
...4444  
..55555  
.666666  
7777777
```  
##### Pattern 3:
###### Solution
```python
for i in range(1, a + 1):
    if i%2 != 0:
        for j in reversed(range(1, i+1)):
            print(j, end = '')
        print('')
    else:
        print(i*str(i))

```
###### Output   
```js
1  
22  
321  
4444  
54321  
666666  
7654321
```  
##### Pattern 4:
###### Solution
```python
print('*')
for i in range(a+1):
    print('*' + i*'-'+'*')
print((a+3)*'*')

```
###### Output   
```js
*
**
*-*
*--*
*---*
*----*
*-----*  
*------*  
*-------*  
**********
```  
##### Pattern 5:  
###### Solution
```python
for i in range(1,a+1):
    arr = []
    for j in range(1, (a + 1)):
        arr.append(0)
    arr[i-1] = i
    arr[-i] = i
    print(arr)

```
###### Output  
```js
1000001  
0200020  
0030300  
0004000  
0050500  
0600060  
7000007
```  
##### Pattern 6:  
###### Solution
```python
for i in reversed(range(1,a+1)):
    print((a-i)*' ' + str(i), end = '')
    print((i-1)*('-' + str(i)))

```
###### Output  
```python
7-7-7-7-7-7-7  
 6-6-6-6-6-6  
  5-5-5-5-5  
   4-4-4-4  
    3-3-3  
     2-2  
      1  
   ```
##### Pattern 7:  
###### Solution
```python
print(a*'+')
for i in range(1,a-2):
    print('+' +((a-2)*'*') +'+')
print(a*'+')

```
###### Output  
```js
+++++++  
+*****+  
+*****+  
+*****+  
+*****+  
+*****+  
+++++++  
```
##### Pattern 8 (you may assume input number is odd):
###### Solution
```python
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

```
###### Output    
```js
+-+-+-+  
-*****+  
+*****-  
-*****+  
+*****-  
-*****+  
+-+-+-+  
```
## Donations
- Bitcoin : 1NwFxut38j6ex8KWEPKuWaikUBYNW476gV <br>
[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/us)

##### or  
## Oh Thanks
By the way... thank you! And if you'd like to [say thanks](https://saythanks.io/to/us)... :)  
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/us)  
✨🍰✨

![alt text](https://github.com/us/ceng1003/blob/master/rick-dede.webp "p4 outputs")


