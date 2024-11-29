'''
*******
 *****
  ***
   *
'''

num = 4
space = 0
star = 2*num-1
for line in range(num):
    print(' ' * space + '*' * star)
    space += 1
    star -= 2
    
