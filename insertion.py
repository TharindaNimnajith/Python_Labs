def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        #while(i >= 0 and A[i] > key):
        while(i >= 0 and A[i] < key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

a = []

for i in range(4):
    a.append(eval(input('Enter: ')))

Insertion_Sort(a)
print(a)
