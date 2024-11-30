#selection sort
#The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.


arr=[4,5,7,23,2]
n=len(arr)
for i in range(n-1):
    min_index=i                    #storing index in min_index
    for j in range(i+1,n):
        if arr[j]< arr[min_index]:
            min_index=j             #allocate j index into mini_index
            arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

# arr=[3,4,65,2,1]
# n=len(arr)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if arr[j]>arr[min_index]:
#             min_index=j
#             min_val=arr.pop(min_index)
#             arr.insert(i,min_val)
# print(arr)