import csv

with open('students.csv', encoding = 'utf8') as f:
    a = list(csv.reader(f, delimiter = ','))[1:]
    d = {a[x][-3]:f'Проект № {a[x][-3]} делал: {a[x][1].split()[0][0]}. {a[x][1].split()[1]} он(а) получил(а) оценку - {a[x][-1]}' for x in range(len(a))}
    numb = input()
    while numb != 'СТОП':
        if numb in d.keys():
            print(d[numb])
        else:
            print('Ничего не найдено')
        numb = input()
