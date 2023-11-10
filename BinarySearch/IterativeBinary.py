import math
def binarySerachIterative (arr , data):
    left = 0
    right = len(arr) - 1
    while left <= right :
        mid = math.floor((left + right) / 2)
        if data == arr [mid]:
            return True
        elif data > arr[mid]:
            left = mid + 1
        else :
            right = mid - 1
    return False
print(binarySerachIterative([1,2,3,4,5,6,7] , 9999))