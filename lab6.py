a = []

for i in range(5):
    no = int(input('Enter a number: '))
    a.append(no)

print(a)

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

InsertionSort(a)
print(a)
