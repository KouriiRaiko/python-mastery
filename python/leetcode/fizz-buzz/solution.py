# https://leetcode.com/problems/fizz-buzz/description/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fizz(n):
            if n % 3 == 0:
                return True
            return False
        
        def buzz(n):
            if n % 5 == 0:
                return True
            return False
        
        output = []
        for i in range(1, n+1):
            if fizz(i) and buzz(i):
                output.append("FizzBuzz")
            elif fizz(i):
                output.append("Fizz")
            elif buzz(i):
                output.append("Buzz")
            else:
                output.append(str(i))
            
        return output