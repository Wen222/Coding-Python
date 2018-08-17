#!/usr/bin/env python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or (x%10==0 and x!=0):
            return False

        
        rev = 0

        while rev < x:
            rev = rev * 10 + x%10
            x //= 10
        return rev == x or rev/10 == x

if __name__ == "__main__":
    print(Solution().isPalindrome(1001))
#    print(Solution().isPalindrome(12320))
#    print(Solution().isPalindrome(-12321))
