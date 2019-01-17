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
        max_num = - 2 ** 31
        this = 0
        for i in range(len(nums)):
            
            if this < 0:
                this = 0
            this = this + nums[i]
            max_num = max(this, max_num)
        return max_num
