# 递归版本
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


# 递归版本2
def quick_sort2(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort2(array, left, q - 1)
        quick_sort2(array, q + 1, right)


def partition(array, left, right):
    key = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= key:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


# 非递归版本
def quick_sort3(array, left, right):
    if left >= right:
        return
    stack = []
    stack.append(left)
    stack.append(right)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if low >= high:
            continue
        key = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= key:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
