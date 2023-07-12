class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            return self.myPow(1/x,-n)
        ans=self.myPow(x,n//2)
        if n%2==0:
            return ans*ans
        else:
            return x*ans*ans