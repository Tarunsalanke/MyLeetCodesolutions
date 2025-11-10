class Solution:
    def isPalindrome(self, x):
        strx=str(x)
        if strx[::-1]==strx:
            return True
        else:
            return False
        
ob=Solution()

if ob.isPalindrome(121):
    print('It is Palindrome')
else:
    print('It is not Palindrome')
