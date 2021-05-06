def recursive_sum(n):
    if (n ==1):
        return 1
    return n + recursive_sum(n-1)

ret = recursive_sum(10)
print(ret)