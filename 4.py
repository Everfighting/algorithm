# 希尔排序
def shell_sort(arry):
    n = len(arry)
    gap = round(n/2)
    while gap > 0 :
        for i in range(gap, n)
            temp = arry[i]
            j = i
            while ( j >= gap and arry[j-gap] > temp ):
                arry[j] = arry[j-gap]
                j = j - gap
            arry[j] = temp
        gap = round(gap/2)
    return arry
