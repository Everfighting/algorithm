# 归并排序
def merge_sort(arry):
    if len(arry) <= 1: return arry
    num = int(len(arry/2))
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left, right)

def merge(left,right):
    l,r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
