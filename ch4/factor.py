def factor(n):
    if n ==1:
        return [1]
    ret = []
    div = 2
    while True:
        if n >1:
            while (n % div ==0):
                n = n / div
                ret.append(div)
            div = div + 1    
        else:
            break
    return ret

a = factor(1999)
print(a)

            
