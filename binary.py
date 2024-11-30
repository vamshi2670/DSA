def binarysearch(arr,targetval):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+right//2
        if arr[mid]==targetval:
            return mid
        if arr[mid]<targetval:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[5,7,3,8,2]
targetval=3
result=binarysearch(arr,targetval)
if result!=-1:
    print(targetval,'found in' ,result,'index')
else:
    print('not found')