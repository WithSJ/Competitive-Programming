def plusMinus(arr):
    # Write your code here
    from operator import neg
    length = len(arr)
    negs = 0
    poss = 0
    zeros = 0

    for i in arr:
        if i < 0:
            negs+=1
        elif i > 0:
            poss+=1
        else:
            zeros+=1

    print("{:.6f}".format(poss/length))
    print("{:.6f}".format(negs/length))
    print("{:.6f}".format(zeros/length))



if __name__ == '__main__':
    plusMinus([-4, 3, -9, 0, 4, 1])
