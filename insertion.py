# arr=[3,6,434,23,1]
# n=len(arr)
# for i in range(1,n):
#     insert_index=i
#     current_val=arr.pop(i)
#     for j in range(i-1,-1,-1):
#         if arr[j]>current_val:
#             insert_index=j
#     arr.insert(insert_index,current_val)
# print(arr)

arr=[4,5,23,1,8]
n=len(arr)
for i in range(1,n):
    insert_index=i               
    current_val=arr[i]
    for j in range(i-1,-1,-1):
        if arr[j]>current_val:       #4>5 
            arr[j+1]=arr[j]
            insert_index=j
        else:
            break
    arr[insert_index]=current_val 
print(arr)