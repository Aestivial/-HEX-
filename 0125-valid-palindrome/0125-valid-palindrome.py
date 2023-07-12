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
            
        def check(x,i,j):
            if i>j:
                return True
            elif x[i]==x[j]:
                return check(x,i+1,j-1)
            else:
                return False
        return check(x,0,len(x)-1)