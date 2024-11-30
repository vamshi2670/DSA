# arr=[12,45,64,7,2,90]
# radixarr=[[],[],[],[],[],[],[],[],[],[]]
# max_val=max(arr)
# exp=1
# while max_val//exp>0:
#     while len(arr)>0:
#         val=arr.pop()
#         radixindex=(val//exp)%10
#         radixarr[radixindex].append(val)
#     for i in radixarr:
#         while len(i)>0:
#             val=i.pop()
#             arr.append(val)
#     exp*=10
# print(arr)


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            bubbleSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)