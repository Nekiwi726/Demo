import csv

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i][-1]
        j = i - 1
        while (j >= 0 and temp > lst[j][-1]):
            lst[j + 1][-1] = lst[j][-1]
            j = j - 1
        lst[j + 1][-1] = temp
    return lst

with open('students.csv', encoding = 'utf8') as f:
    reader = csv.reader(f, delimiter = ',')
    a = [x for x in reader if '10' in x[-2]]
    b = insertion_sort(a)[:3]
    for i in range(len(b)):
        print(f'{i+1} место: ' + b[i][1].split()[1][0] + '. ' + b[i][1].split()[0])
