
from pip import main

def lonelyinteger(a):
    # Write your code here
    arr = dict()
    for i in a:
        arr[i] = a.count(i)

    for k,v in arr.items():
        if v == 1:
            return k

if __name__ == "__main__":
    a = [1,2,3,4,3,2,1]
    print(lonelyinteger(a))