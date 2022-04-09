arr = [0,1,2,4,6,5,3]

arr.sort()
lenth = len(arr)
if lenth % 2 == 0 :
    median = arr[lenth//2] + arr[ (lenth//2) -1] 
    print(arr,median/2)
else:
    print(arr[lenth//2])