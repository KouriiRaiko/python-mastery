# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        def is_mountain(i):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return True
            return False
        
        for i in range(1, len(A)):
            if is_mountain(i):
                return i
                