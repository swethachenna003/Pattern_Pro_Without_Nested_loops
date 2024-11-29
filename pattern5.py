'''
*****
 ****
  ***
   **
    *
'''

num = 5
space = 0
star = num-1
for line in range(num):
    print(' ' * space + '*' * star)
    space += 1
    star -= 1
    
