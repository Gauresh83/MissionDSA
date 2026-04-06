class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obSet=set()
        for (x, y) in obstacles:
            obSet.add((x, y))
        dir=[(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y,dx, dy, face, maxD2=0, 0, 0,1, 0, 0
        for  c in commands:
            if c==-2:
                face=(face+1)&3
                dx=dir[face][0]
                dy=dir[face][1]
            elif c==-1:
                face=(face+3)&3
                dx=dir[face][0]
                dy=dir[face][1]
            else:
                for i in range(c):
                    x+=dx
                    y+=dy
                    if (x, y) in obSet:
                        x-=dx
                        y-=dy
                        break
                maxD2=max(maxD2, x*x+y*y)
        return maxD2
