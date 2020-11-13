x = 0
y = 0
j = 0
i = 0
k = 0


def foo1(x,y,i,j,k):
    for i in range(10):
        print(f"{y} + {i}")
        y = y + i
        print(f"New y: {y}")
        k = i + j
        print(f"{k} = {i} + {j}")
    print(f"foo1: x: {x} and y: {y} i: {i} j: {j} k: {k}")

def foo2(x,y,i,j,k):

    j = x + y
    print(f"before foo1 j: {j}")
    foo1(x,y,i,j,k)
    k = j + i
    i = k + j
    print(f"foo2: x: {x} and y: {y} i: {i} j: {j} k: {k}")


x = 10
y = 5
print(f"Main: x: {x} and y: {y}")
foo2(x,y,i,j,k)






