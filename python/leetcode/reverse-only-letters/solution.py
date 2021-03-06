# https://leetcode.com/problems/reverse-only-letters/description/

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        letters = []
        
        S = list(S)
        
        for letter in S:
            if letter.isalpha():
                letters.append(letter)
        
        for i, letter in enumerate(S):
            if letter.isalpha():
                S[i] = letters.pop()
                
        
        return ''.join(S)