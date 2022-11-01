class Solution(object):
    def isPalindrome(self,x):
        x = str(x)
        return x.lower() == x[::-1].lower()
