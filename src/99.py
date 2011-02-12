from math import log

max = 0
max_line = 0
f = open('../base_exp.txt')
for i,line in enumerate(f):
    a,b = [int(i) for i in line.strip().split(',')]
    val = b * log(a)
    print(val)
    if val > max:
        max = val
        max_line = int(i)
print(max_line+1)
