import recursion
import memoize
import bottoms_up
import time

# Chase Staples
# Showing different Fib() functions and their complexity
# Using dynamic programming to show these complexities
# Basic Recursion, Memoize method, and Bottoms Up method


# Calling Recursive Fib() function
# Double Check: I can't start at 0 will return a recursion error
n = 21
print("              Fibonacci Recursion Method             ")
print("-------------------------------------------------------------------------------------")
startTime = time.time()
print(f"Start Time: {startTime}")
for i in range(1,n):
        print(f" {recursion.fib(i)} ", end="")
time.sleep(.5)
endTime = time.time()
timing = endTime - startTime
timing = '{0:.3f}'.format(timing)
print(f"\nEnd Time: {endTime}")
print(f"Time: {timing} secs")
print("-------------------------------------------------------------------------------------")

# Calling Memoize Fib() function
print("              Fibonacci Memoize Method             ")
print("-------------------------------------------------------------------------------------")
startTime2 = time.time()
print(f"Start Time: {startTime2}")
for i in range(1,n):
        print(f" {memoize.fib_memo(i)} ", end="")
time.sleep(.5)
endTime2 = time.time()
timing2 = endTime2 - startTime2
timing2 = '{0:.3f}'.format(timing2)
print(f"\nEnd Time: {endTime2}")
print(f"Time: {timing2} secs")
print("-------------------------------------------------------------------------------------")

# Calling Bottoms Up Fib() function
print("              Fibonacci Bottoms Up Method             ")
print("-------------------------------------------------------------------------------------")
startTime3 = time.time()
print(f"Start Time: {startTime3}")
for i in range(1,n):
        print(f" {bottoms_up.fib_bottom_up(i)} ", end="")
time.sleep(.5)
endTime3 = time.time()
timing3 = endTime3 - startTime3
timing3 = '{0:.3f}'.format(timing3)
print(f"\nEnd Time: {endTime3}")
print(f"Time: {timing3} sec")
print("-------------------------------------------------------------------------------------")