import csv
import random
import string

def create_login(lst):
    name = lst[1].split()
    return name[0] + '_' + name[1][0] + name[2][0]

def create_password():
    s = string.ascii_letters + string.digits
    return ''.join(random.choice(s) for i in range(8))

with open('students.csv', encoding = 'utf8') as f:
    a = list(csv.reader(f, delimiter = ','))[1:]
    a = [i + [create_login(i)] + [create_password()] for i in a]

with open('students_password.csv', 'w', encoding = 'utf8', newline = '') as f:
    w = csv.writer(f)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    w.writerows(a)
