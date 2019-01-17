"""
Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        this = 0
        max_sum = - 2 ** 31
        for i in range(len(nums)):
            
            this = this + nums[i]
            max_sum = max(this, max_sum)
            if this < 0:
                this = 0
                continue
        return max_sum


