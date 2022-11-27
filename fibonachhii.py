# method 1 usint iter method -- this method is so faster than recursion method
import time
def fiboiter(n):
    prevno = 0
    currentno = 1
    for i in range (1,n):
        prevprevno = prevno
        prevno = currentno
        currentno = prevno + prevprevno
    return currentno
if __name__ == "__main__":
    num = int(input("Enter the num:- "))
    init = time.time()
    print(fiboiter(num))
    print(f"It took {time.time()-init} seconds")


#method 2 using recursion method

def fiborec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiborec(n-1) + fiborec(n-2)
if __name__ == "__main__":
    num = int(input("Enter the num:- "))
    init = time.time()
    print(fiborec(num))
    print(f"It took {time.time()-init} seconds")
