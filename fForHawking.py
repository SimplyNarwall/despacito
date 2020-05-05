"""
ID: kevinsh4
LANG: PYTHON3
TASK: wormhole
"""
from itertools import combinations, permutations
#einstein = open('wormhole.in')
#written = open('wormhole.out')
einstein = open('C:/Users/kevin/OneDrive/Documents/SNAAAKES/noMoreUSACO/frickEpstein')
written = open('C:/Users/kevin/OneDrive/Documents/SNAAAKES/noMoreUSACO/noonewantstodothis', 'w')

def rotations(data):
   datadata = data + data
   l = len(data)
   for i in range(l):
       yield datadata[i:i+l]


def pairs(d, ata):
   if len(ata) == 1:
      yield [[d]+ata]
   else:
      for rotation in rotations(ata):
         for p in pairs(rotation[1], rotation[2:]):
            yield [[d,rotation[0]]] + p

def make_pairs(data):
   return pairs(data[0], data[1:])

def gdSucks(data):
    #print(data)
    for i in range(wormholeCount//2):
        #print(data)
        desiredPos = data[i][0]
        pos = data[i][0]
        for y in range(wormholeCount): #only allow Bessie to go so many steps
            try:
                nextPos = min(wh for wh in coordinates if wh[1] == pos[1] and wh[0] > pos[0])
            except ValueError:
                break
            for foo in (data):
                if nextPos in foo:
                    pos = foo[1] if foo.index(nextPos) == 0 else foo[0]
            #print(pos, desiredPos)
            if pos == desiredPos: return True
    else:
        for i in range(wormholeCount//2):
            desiredPos = data[i][1]
            pos = data[i][1]
            for y in range(wormholeCount): #only allow Bessie to go so many steps
                try:
                    nextPos = min(wh for wh in coordinates if wh[1] == pos[1] and wh[0] > pos[0]) #calculates the wormhole closest
                except ValueError:
                    break
                for foo in (data):
                    if nextPos in foo:
                        pos = foo[1] if foo.index(nextPos) == 0 else foo[0]
                #print(pos, desiredPos)
                if pos == desiredPos: return True
    return False

coordinates = []
for v, line in enumerate(einstein):
    if v != 0:
        coordinates.append([int(x) for x in line.rstrip().split()])
    else:
        wormholeCount = int(line.rstrip())

count = 0
for comb in make_pairs(coordinates): #sees if anything is valid (with repeats)
    if gdSucks(comb):
        print(comb, 'worked')
        count += 1
    else:
        print(comb)
#correct answer for run 8 is 8790
written.write(str(count) + '\n')