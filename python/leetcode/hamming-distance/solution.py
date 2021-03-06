# https://leetcode.com/problems/hamming-distance/description/

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        differences = bin(x ^ y)
        
        difference_count = differences.count("1")
        return difference_count