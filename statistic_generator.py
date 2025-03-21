from random import uniform
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

min = int(input('Min: '))
max = int(input('Max: '))
up = int(input('Up: '))
down = int(input('Down: '))
count = int(input('Count: '))
plt1 = input('Plt(T or F): ')

if plt1 == 'T':
    plt1 = True
elif plt1 == 'F':
    plt1 = False

a = int(uniform(min, max) // 1)
b = 0
y = []
x = []
for i in range(0, count):
    c = b
    b = a
    a = int(uniform(a+up, a-down) // 1)
    if a < min:
        a = 3
    elif a > max:
        a = 200
    elif ((b/3)//1) < ((a/3)//1) and ((b/3)//1) > ((c/3)//1):
        symvol = '\\'
        '''
            |-\\   c
            |--\\  b
            |---\\ a
        '''
    elif ((b/3)//1) > ((a/3)//1) and ((b/3)//1) < ((c/3)//1):
        symvol = '/'
        '''
            |---/ c
            |--/  b
            |-/   a
        '''
    elif ((b/3)//1) == ((a/3)//1) and ((b/3)//1) == ((c/3)//1):
        symvol = '|'
        '''
            |--| c
            |--| b
            |--| a
        '''
    if ((b/3)//1) > ((a/3)//1) and ((b/3)//1) > ((c/3)//1):
        symvol = ')'
        '''
            |-\\  c
            |--) b
            |-/  a
        '''
    if ((b/3)//1) < ((a/3)//1) and ((b/3)//1) < ((c/3)//1):
        symvol = '('
        '''
            |--/ c
            |-(  b
            |--\\ a
        '''
    if not plt1:
        print('|' + '-'*int((int(b)/3)//1) + symvol)
        sleep(0.15)
    y.append(b)
    x.append(i)
if plt1:
    plt.plot(x, y)
    plt.show()
#print(x, y)
if not plt1:
    input()