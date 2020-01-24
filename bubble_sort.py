def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if(A[j] < A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]
                #temp = A[j]
                #A[j] = A[j - 1]
                #A[j - 1] = temp

a = []

for i in range(8):
    a.append(eval(input('Enter a number: ')))

print(a)

BubbleSort(a)
print(a)
