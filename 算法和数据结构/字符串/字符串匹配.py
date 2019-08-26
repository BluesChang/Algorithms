# 暴力求解
def str_match(s, p):
    m = len(s)
    n = len(p)
    for i in range(m - n + 1):
        if s[i:i + n] == p:
            return True
    return False


# KMP算法
def kmp_match(s, p):
    # 部分匹配表
    def partial_table(p):
        prefix = set()
        postfix = set()
        table = [0]
        for i in range(1, len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            table.append(len((prefix & postfix or {''}).pop()))
        return table

    m = len(s)
    n = len(p)
    cur = 0
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            return True
    return False

print(str_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
