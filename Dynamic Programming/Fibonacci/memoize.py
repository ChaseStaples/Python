def fib(number, memo):
    if(memo[number] != None):
        return memo[number]
    if (number == 1 or number == 2):
        result = 1
    else:
        result = fib(number - 1, memo) + fib(number - 2, memo)
    memo[number] = result
    return result

def fib_memo(number):
    memo = [None] * (number + 1)
    return fib(number, memo)

# As number increase to roughly number > 1000
# A recursion errpr may occur do to no enough room and
# too many recursive calls on the call stack