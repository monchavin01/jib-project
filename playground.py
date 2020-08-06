a = 1
b = "string"
c = True
print(a, b ,c)
d = b + ' hello'
print(d)

print(f'c is {c}, a is {a}, b is {b}')

l = [1, 2, 3, '4']
print(f'list is {l}')
t = (1, 2, 3, 4)
print(f'tuple is {t}')
dt = {
    'name': 'golf',
    'team': 'odds',
}
print(f'dt is {dt}')

print(f'l at index 0 : {l[0]}')
print(f't at index 1 : {t[1]}')
print(f'dt at key team : {dt["team"]}')


if a == 1:
    print(a)
    print('true')
elif a == 2:
    print('equal 2')
else:
    print('not 1')

l = [1, 2, 3, 4, 5]
for item in l:
        print(item)
        if item == a:
            print('yeah')
            print('hey!')
for item in dt:
    print(dt[item])
print(dt.items())
print(dt.keys())
print(dt.values())