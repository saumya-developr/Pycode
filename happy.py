num=int(input('enter a number'))
for k in range (1,num):
    for j in range (1,num-k):
       print('  ',end='')
    for i in range (1,num*2-1):
        print('*',end='')
    print()   