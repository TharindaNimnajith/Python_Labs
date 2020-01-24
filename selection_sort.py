def SelectionSort(A):
    n = len(A)
    for j in range(n - 1):
        smallest = j
        for i in range(j + 1, n):
            if(A[i] < A[smallest]):
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

a = []

for i in range(5):
    a.append(eval(input('Enter: ')))

print(a)

SelectionSort(a)
print(a)
