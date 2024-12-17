def findDisappearedNumbers(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            arr[i],arr[correct_index] = arr[correct_index],arr[i]
        else:
            i += 1

    res = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            res.append(i+1)
    return res
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
            
        
        
        
        