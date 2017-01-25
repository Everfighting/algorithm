# 冒泡算法
def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for j in rang(1,n-1):
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j],arry[j-1]
    return arry
