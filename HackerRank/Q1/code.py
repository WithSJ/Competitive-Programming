#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    outputList = list()
    for i in arr:
        tempArr = arr.copy()
        tempArr.remove(i)
        outputList.append(sum(tempArr))

    print(min(outputList),max(outputList))

miniMaxSum([1,2,3,4,5])