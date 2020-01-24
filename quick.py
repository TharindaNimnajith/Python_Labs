def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        #if(A[j] <= x):
        if(A[j] >= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
    
def Quick_Sort(A, p, r):
    if(p < r):
        q = Partition(A, p, r)
        Quick_Sort(A, p, q - 1)
        Quick_Sort(A, q + 1, r)

a = []

for i in range(4):
    a.append(eval(input('Enter: ')))

Quick_Sort(a, 0, 3)
print(a)
