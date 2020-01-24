no1 = input('Enter no1: ')
no2 = input('Enter no2: ')
no3 = input('Enter no3: ')

if (no1 < no2 and no1 < no3):
    min = no1
elif (no2 < no3):
    min = no2
else:
    min = no3

print(min)
