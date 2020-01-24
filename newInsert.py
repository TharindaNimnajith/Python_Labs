def Insertion_Sort(A):
    for j in range(1, len(A)):
        i = 0
        while(A[j] < A[i]):
            i = i + 1
        key = A[j]
        for k in range(j - i):
            A[j - k] = A[j - k - 1]
        A[i] = key

a = []

for i in range(10):
    a.append(eval(input('Enter: ')))

Insertion_Sort(a)
print(a)
