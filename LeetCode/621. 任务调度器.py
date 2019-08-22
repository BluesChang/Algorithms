class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        task_map = dict()
        for i in tasks:
            task_map[i] = task_map.get(i, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        max_task_sum = task_sort[0][1]
        res = (max_task_sum - 1) * (n + 1)
        for i in task_sort:
            if i[1] == max_task_sum:
                res += 1
        return res if res >= length else length
