def findMax(nums):
    result = nums[0] # assume first number is the maximum one
    max2 = nums[1]
    for num in nums[1:]: # check the rest of the numbers
        if num > result:
            result = num # if you find a larger num than the return result # current one found, modify your result
    print(result)

#findMax([4,6,1,7,8,9])

arr = [9999,6,1,7,8,9,61,251,2351,523,5,5,600,500,700]
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