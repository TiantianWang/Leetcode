"""
Description

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s == ' ':
            return 0        
        count = 0 
        for i in range(len(s)-1, -1, -1):

            if s[i] != ' ':
                count = count +1
                if s[i-1] == ' ':
                    break
            if s[i] == ' ':
                continue
        return count
