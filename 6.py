# 快速排序
def quick_sort(arry):
    return qsort(arry,0,len(arry)-1)

def qsort(arry,left,right):
    if left >= right: return arry
    key = arry[left]
    lp = left
    rp = right
    while lp < rp:
        while arry[rp] >= key and lp < rp：
            rp -= 1
        while arry[lp] <= key and lp < rp：
            lp += 1
        arry[lp],arry[rp] = arry[rp],arry[lp]
    arry[left],arry[lp] = arry[lp],arry[left]
    qsort(arry,left,lp-1)
    qsort(arry,rp+1,right)
    return arry
