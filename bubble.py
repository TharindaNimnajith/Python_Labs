def Bubble_Sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if(A[j] > A[j - 1]):
            #if(A[j] < A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]

a = []

for i in range(4):
    a.append(eval(input('Enter: ')))

Bubble_Sort(a)
print(a)