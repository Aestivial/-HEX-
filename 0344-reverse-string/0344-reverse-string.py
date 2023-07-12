class Solution:
    def reverseString(self, s: List[str]) -> None:
        def func(s,i,j):
            if i>j:
                return s
            s[i],s[j]=s[j],s[i]
            return func(s,i+1,j-1)
        print(func(s,0,len(s)-1))