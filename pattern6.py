'''
    *
   ***
  *****
 *******
*********
'''

num = 5
space = num-1
star = 1
for line in range(num):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2
    
