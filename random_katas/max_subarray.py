def max_crossing_subarray(a,low,mid,high):
    left_sum = -999999
    suma = 0
    max_left,max_right=0,0
    for i in range(mid,low,-1):
        suma+=a[i]
        if suma>left_sum:
            left_sum = suma
            max_left = i
    right_sum=-9999999
    suma = 0
    for j in range(mid+1,len(a)):
        suma +=a[j]
        if suma>right_sum:
            right_sum=suma
            max_right = j
    return left_sum+right_sum
def max_subarray(a,low,high):
    if high == low:
        return a[low]
    else:
        mid = (high+low)//2
        return (max(max_subarray(a,low,mid),max_subarray(a,mid+1,high),max_crossing_subarray(a,low,mid,high)))
    
a = [-3,10,6,-1,0,-5,26]
print(max_subarray(a,-1,len(a)-1))
