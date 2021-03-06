# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        
        letters_numbers = zip(letters, numbers)
        dictionary = dict(letters_numbers)     
        
        def letter_value(l, power):
            if power > 0:
                return dictionary[l] * 26 ** power
            else:
                return dictionary[l]
            
        sum = 0
        for i in range(0, len(s)):
            power = len(s) - 1 - i
            sum += letter_value(s[i], power)
            
        return sum
            
                