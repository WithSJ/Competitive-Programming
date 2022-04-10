def diagonalDifference(arr):
    # Write your code here
    index = 0
    LR = 0
    RL = 0
    for item in arr:
        LR += item[index]
        RL += item[(len(item)-1)-index]
        index +=1

    return abs(LR - RL)


if __name__ == '__main__':
    arr = [ [1,2,3],
            [4,5,6],
            [9,8,9]]
    
    result = diagonalDifference(arr)
    print(result)

    