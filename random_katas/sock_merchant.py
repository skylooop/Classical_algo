'''
Input Format:
The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Output Format:
Return the total number of matching pairs of socks that John can sell.
'''
def sockMerchant(n, ar):
    data = {}
    for i in range(len(ar)):
        data[ar[i]] = ar.count(ar[i])//2
    return sum(data.values())
