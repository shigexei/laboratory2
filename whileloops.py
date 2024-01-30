i = 1
while i < 6:
    print(i)
    i+=1
'''
1
2
3
4
5
'''
j = 1
while j < 6:
    print(j)
    if j==3:
        break
    j+=1
    
'''
1
2
3
'''

k = 0 
while k < 6:
    k+=1
    if k==3:
        continue
    print(k)

'''
1
2
4
5
6

'''
l = 1 
while l < 6:
    print(l)
    l+=1
else:
    print('i is no longer less than 6')