"""
使用递归法求解列表中的最大的元素
"""

def find_max_int(data,n):
    if n == 1:
        return data[0]
    else:
        x = find_max_int(data,n-1)
        return x if x > data[n-1] else data[n-1]


data = [6,3,6,1,1]
print(find_max_int(data,len(data)))
