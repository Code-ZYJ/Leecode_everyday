'''
input 的第一行是n、m、k，代表地图的行、列以及小偷逃走的次数
第二行到n+1行是地图
n+2行到最后是小偷逃跑的方向
以这个图为例(0,0)->(1,3)->(1,2)->(0,2)
'''


input= [['3','4','4'],
        ['@','.','.','.'],
        ['.','#','.','.'],
        ['.','.','.','#'],
        ['EAST'],
        ['SOUTH'],
        ['WEST'],
        ['NORTH']]

n,m,k = int(input[0][0]),int(input[0][1]),int(input[0][2])
map=[]
for i in range(1,n+1):
    map.append(input[i])
allfx = []
for i in range(n+1,n+1+k):
    allfx.append(input[i])

def loc_init(map):
    for i in range(len(map)):
        if '@' in map[i]:
            j = map[i].index('@')
            return [i, j]

import numpy as np
def move(loc,fx,map):
    map = np.array(map)
    x,y = loc[0],loc[1]
    if fx ==['EAST']:
        if '#' not in map[x,y:]:
            loc = [x,m-1]
        else:
            loc = [x,list(map[x,y:]).index('#')-1]
    if fx ==['SOUTH']:
        if '#' not in map[x:,y]:
            loc = [n-1,y]
        else:
            loc = [list(map[x:,y]).index('#')-1,y]
    if fx == ['WEST']:
        if '#' not in map[x,:y]:
            loc = [x,0]
        else:
            loc = [x,list(map[x,:y]).index('#')+1]
    if fx == ['NORTH']:
        if '#' not in map[:x,y]:
            loc = [0,y]
        else:
            loc = [list(map[:x,y]).index('#')+1,y]
    return loc

loc =loc_init(map)
for fx in allfx:
    loc=move(loc, fx,map)
    print(loc)
print(loc)


