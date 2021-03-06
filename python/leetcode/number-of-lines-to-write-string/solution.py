# https://leetcode.com/problems/number-of-lines-to-write-string/description/

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        dictionary = dict(zip(alphabet, widths))
        
        rows = 1
        filled = 0
        
        S = list(S)[::-1]
        while(S):
            next_letter = S.pop()
            if filled + dictionary[next_letter] <= 100:
                filled += dictionary[next_letter]
            else:
                rows += 1
                filled = 0
                filled += dictionary[next_letter]
            
        return [rows, filled]
            