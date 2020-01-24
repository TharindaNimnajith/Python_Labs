def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] < key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

a = []

for n in range(5):
    no = eval(input('Enter a number between 10 to 20: '))
    while(no < 10 or no > 20):
        print('Invalid number... Try again')
        no = eval(input('Enter a number between 10 to 20: '))
    a.append(no)

InsertionSort(a)
print(a)
