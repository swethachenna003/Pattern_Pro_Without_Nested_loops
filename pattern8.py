'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

num = 9
space = num//2
star = 1
for line in range(num//2+1):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2
space = 1
star = num-2
for line in range(num//2):
    print(' ' * space + '*' * star)
    space += 1
    star -= 2

    
