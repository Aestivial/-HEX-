class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalpha():
                x+=i.lower()
            elif i.isdigit():
                x+=str(i)
            else:
                pass
            
        return x==x[::-1]