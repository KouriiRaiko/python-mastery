# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        ops = list(ops)
        points = []
        
        while ops:
            curr = ops.pop(0)
            if curr == "+":
                points.append(points[-1] + points[-2])
            elif curr == "D":
                points.append(points[-1] * 2)
            elif curr == "C":
                del points[-1]
            else:
                points.append(int(curr))
                
        return sum(points)