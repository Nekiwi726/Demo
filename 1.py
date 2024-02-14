import csv

with open('students.csv', encoding = 'utf8') as f:
    a = list(csv.reader(f, delimiter = ','))[1:]
    cls = {x[-2]:[0, 0] for x in a}
    for i in a:
        if i[-1] != 'None':
            cls[i[-2]][0] += 1
            cls[i[-2]][1] += int(i[-1])
    cls = {x:round(cls[x][1] / cls[x][0], 3) for x in cls.keys()}

    for i in range(len(a)):
        if a[i][-1] == 'None':
            a[i][-1] = cls[a[i][-2]]
        if 'Хадаров Владимир' in a[i][1]:
            print(f'Ты получил: {a[i][-1]}, за проект - {a[i][-3]}')

with open('student_new.csv', 'w', encoding = 'utf8', newline = '') as f:
    w = csv.writer(f)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writerows(a)
