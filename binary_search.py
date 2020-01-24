def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def BinarySearch(A, min, max, key):
    if(max < min):
        return False
    else:
        mid = (min + max) / 2
        if(A[mid] > key):
            return BinarySearch(A, min, mid - 1, key)
        elif(A[mid] < key):
            return BinarySearch(A, mid + 1, max, key)
        else:
            return mid


a = []

for i in range(8):
    a.append(eval(input('Enter a number: ')))

print()
print(a)
print()

InsertionSort(a)
print(a)
print()

position = BinarySearch(a, 1, 100, 40)
print(position)
