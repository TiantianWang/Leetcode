"""
Description

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

class Solution(object):
    def isPalindrome(self, s):  
    """
    :type s: str
    :rtype: bool
    """
    if not s: return True
    l, r = 0, len(s)-1
    while l < r:
      sl = s[l].lower()
      sr = s[r].lower()
      if s[l].isalnum() and s[r].isalnum():
        if sl != sr:
          return False
        l += 1
        r -= 1
      else:
        if not s[l].isalnum():
          l += 1
        if not s[r].isalnum():
          r -= 1
    return True
