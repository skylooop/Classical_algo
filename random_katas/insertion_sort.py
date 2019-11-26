def insertion(a):
    for j in range(1,len(a)):
        key = a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1],a[i] = a[i],a[i+1]
            i-=1
        a[i+1],key = key,a[i+1]
    return a
