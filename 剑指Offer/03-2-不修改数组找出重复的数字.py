'''
题目：
在一个长度为n+1的数组里的所有数字都在1-n的范围内，所以数组中至少有一个数字是重复的，请找出数组中任意一个重复的数字，
但不能修改输入的数组，例如，如果输入长度为8 的数组 [ 2, 3, 5, 4, 3, 2, 6, 7 ] 那么对应的输出是重复的数字2或者3。
'''


# 方法一：创建一个长度为n+1的辅助数组，然后逐一把原数组的每个数字复制到辅助数组。如果原数组中被复制的数字是m，则把它复制
# 到辅助数组中下标为m的位置。这样很容易发现哪个数字是重复的。
# 空间O(n)

def duplicate1(arr):
    if not isinstance(arr, list):
        return -1
    length = len(arr)
    for i in range(length):
        if not isinstance(arr[i], int):
            return -1
        if arr[i] < 1 or arr[i] > length - 1:
            return -1
    Auxiliary = [0 for i in range(length - 1)]
    for i in range(length):
        if Auxiliary[arr[i]] == 0:
            Auxiliary[arr[i]] = arr[i]
        else:
            return arr[i]
    return -1


# 方法二：把从1~n的数字从中间的数字m分为两部分，前面一半为1~m，后面一半为m+1~n。如果1~m的数字的数目超过m，那么这一半的
# 区间里一定包含重复的数字：否则，另一半m+1~n的区间里一定包含重复的数字。
# 时间O（nlogn）空间O(1)
def duplicate2(arr):
    if not isinstance(arr, list):
        return -1
    length = len(arr)
    for i in range(length):
        if not isinstance(arr[i], int):
            return -1
        if arr[i] < 1 or arr[i] > length - 1:
            return -1
    start = 1
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        count = count_number(arr, start, middle)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return -1


def count_number(arr, start, end):
    count = 0
    for i in range(len(arr)):
        if start <= arr[i] <= end:
            count += 1
    return count


# 测试用例
# 长度为n的数组里包含一个或多个重复的数字
test_case1 = [2, 3, 1, 4, 3, 2, 5, 7]
# 数组中不包含重复的数字
test_case2 = [1, 2, 3, 4, 5, 6, 7, 8]
# 无效输入测试用例
test_case3 = None

print("----------测试 方法一----------")
print("test_case1:", duplicate1(test_case1))
print("test_case2:", duplicate1(test_case2))
print("test_case3:", duplicate1(test_case3))

print("----------测试 方法二----------")
print("test_case1:", duplicate2(test_case1))
print("test_case2:", duplicate2(test_case2))
print("test_case3:", duplicate2(test_case3))
