def bins(l,r,a):
    mid = (l + r) // 2
    if a[mid] == 0:
        r = mid
    else:
        l = mid
    if r - l == 1:
        return r
    else:
        return bins(l,r,a)

s = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
print(bins(0,len(s)-1,s))
s = list("1" * 14156126136 + "0" * 12314)
print(bins(0,len(s)-1,s))



