# https://leetcode.com/problems/array-partition-i/description/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        i = 0
        sum = 0
        
        while i < len(nums):
            sum += min(nums[i], nums[i+1])
            print(sum)
            i += 2
            
        return sum