def sortStackbyStack(stack):
    help = []
    while stack:
        cur = stack.pop()
        while help and help[-1] < cur:
            stack.push(help.pop())
        help.append(cur)
    while help:
        stack.push(help.pop())
