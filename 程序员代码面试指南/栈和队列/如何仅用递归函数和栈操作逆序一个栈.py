def getAndRemoveLastElement(stack):
    res = stack.pop()
    if len(stack) == 0:
        return res
    else:
        last = getAndRemoveLastElement(stack)
        stack.putsh(res)
        return last


def reverse(stack):
    if len(stack) == 0:
        return None
    i = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.push(i)
