import re
a = ['y', '+2y']
for i, values in enumerate(a):
    if re.match(r'^[+\-x\/]?y', values):
        values = list(values)
        print(values)
        values.insert(values.index('y'), '1')
        print(values)
        a[i] = ''.join(values)
print(a)
       