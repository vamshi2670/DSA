#finding target value in array 

def linearsearch(arr,target_val):
    for i in range(len(arr)):
        if arr[i]==target_val:
            return i
    return -1
arr=[3,5,2,7,9]
target_val=9
result=linearsearch(arr,target_val)
if result!=-1:
    print(target_val,'found in index of',result)
else:
    print('not found')