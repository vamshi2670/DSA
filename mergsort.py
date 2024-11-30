#spliting and merging
#divide-conquer sorting array

def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    sortedleft=mergesort(lefthalf)
    sortedright=mergesort(righthalf)
    return merge(sortedleft,sortedright)
def merge(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
unsorted_arr=[3,6,5,2,5,8,9]
print(mergesort(unsorted_arr))