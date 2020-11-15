def fib_bottom_up(number):
    if (number == 1 or number == 2):
        return 1
    bottom_up = [None] * (number + 1) # memo
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, number + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[number]



# No need for putting recursive calls on a
# call stack so number > can be greater than
# 1000 for more computations