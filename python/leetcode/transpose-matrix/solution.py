# https://leetcode.com/problems/transpose-matrix/description/

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[0 for x in range(len(A))] for y in range(len(A[0]))] 
        
        for r in range(0, len(B)):
            for i in range(0, len(B[r])):
                B[r][i] = A[i][r]
                
        return B