# https://leetcode.com/problems/smallest-range-i/description/

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        A_min = min(A)
        A_max = max(A)
        
        if A_max - A_min > K * 2:
            A_min = A_min + K
            A_max = A_max - K
            return A_max - A_min
        else:
            return 0