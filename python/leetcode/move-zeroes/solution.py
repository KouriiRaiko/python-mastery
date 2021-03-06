# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """    
        
        zero_count = 0
        while 0 in nums:
            nums.remove(0)
            zero_count += 1
            
        for i in range(0, zero_count):
            nums.append(0)