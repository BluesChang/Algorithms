def heap_sort(array):
    def adjust_heap(array, i, size):
        left = i * 2 + 1
        right = i * 2 + 2
        max_index = i
        if left < size and array[left] > array[max_index]:
            max_index = left
        if right < size and array[right] > array[max_index]:
            max_index = right
        if max_index != i:
            array[max_index], array[i] = array[i], array[max_index]
            adjust_heap(array, max_index, size)

    def build_heap(array, size):
        for i in range(size)[::-1]:
            adjust_heap(array, i, size)

    size = len(array)
    build_heap(array, size)
    for i in range(size)[::-1]:
        array[0], array[i] = array[i], array[0]
        adjust_heap(array, 0, i)
    return array
