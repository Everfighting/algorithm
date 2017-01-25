#选择排序
def select_sort(arry):
    n = len(arry)
    for i in range(0,n)
        min = i
        for j in range(i+1,n):
            if arry[j] < arry[min]
                min = j
        arry[min],arry[i] = arry[i],arry[min]
    return arry
