'''
  *****
   ***
    *
   ***
  *****
  
'''

num = 5
space = 0
star = num
for line in range(num//2+1):
    print(' ' * space + '*' * star)
    space += 1
    star -= 2
space = num//2-1
star = 3
for line in range(num//2):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2

    
