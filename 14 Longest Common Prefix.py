"""
Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        cp = ''
        l = [len(st) for st in strs] #lengths for each string
        for i in range(min(l)): # scan from first letter to min str lengths
            tmp = [s[i] for s in strs] #get i-th letter from each string
            if min(tmp)==max(tmp): #check if all of them are the same
                cp = cp + tmp[0]
            else:
                return cp
        return cp
