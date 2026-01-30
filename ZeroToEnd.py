def MoveZerosToEnd(arr,n):
    j=-1
    for i in range(0,n):
        if arr[i]==0:
            j=i
            break

    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j]= arr[j],arr[i]
            j+=1

    return arr

arr= [1,2,0,4,0,5,0,3,5,6,4,0,0]
n=13

print("Values:",MoveZerosToEnd(arr,n))
        
