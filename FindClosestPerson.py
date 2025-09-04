class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d = (x - y) * (x + y - 2 * z)
        return (d > 0) << 1 | (d < 0)
      


                

   
