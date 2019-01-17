"""
Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        intMax = 2**31-1
        intMin = -2**31
        rev = 0
        sign = 1
        if x > intMax or x < intMin:
            return 0
        if x < 0:
            sign = -1
            x *= sign 
        while x != 0:
            pop = x % 10
            x = int(x/10)
            rev = rev * 10 + pop
        return 0 if rev>intMax or rev<intMin else rev*sign
