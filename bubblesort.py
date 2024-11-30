#lowest to highest

arr=[4,2,54,34,1,6]
n=len(arr)

for i in range(n-1):               #5
    for j in range(n-i-1):          #6-2-2
        if arr[j]>arr[j+1]:         #4>2 -> swappe
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


#improve time complexity

for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
print(arr)