def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr = [78, 89, 21, 32, 7, 88]
bubble_sort(arr)
print(arr)

