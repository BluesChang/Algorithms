def insertion_sort(array):
    for i in range(len(array) - 1):
        cur_num = array[i + 1]
        pre_index = i
        while pre_index >= 0 and cur_num < array[pre_index]:
            array[pre_index + 1] = array[pre_index]
            pre_index -= 1
        array[pre_index + 1] = cur_num
    return array
