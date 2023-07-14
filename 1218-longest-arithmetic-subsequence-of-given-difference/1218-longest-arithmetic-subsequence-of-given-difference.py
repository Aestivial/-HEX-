class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d={}
        m=1
        for i in arr:
            if (i-difference) not in d:
                d[i]=1
            else:
                d[i]=d[i-difference]+1
            m=max(m,d[i])
        return m