# Exercise 2
# Question : 11


a=eval(input('Provide the height of the box: '))
b=eval(input('Provide the width of the box: '))
d=a-2
r=b-2

if a >= 1:
    print('*'*b)
if a > 1:
    for i in range(d):
        print('*',end='')
        for i in range(r):
            print(' ',end='')
        print('*')
    print('*'*b,end='')
