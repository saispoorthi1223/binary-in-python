def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

arr = [6,7,8,9,10,11]
target = 8

print(binary_search(arr,target))