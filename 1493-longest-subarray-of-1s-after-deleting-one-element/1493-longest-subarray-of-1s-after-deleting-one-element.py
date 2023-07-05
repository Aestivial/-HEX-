class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=0
        a=[]
        if 0 not in nums:
            return len(nums)-1
        for i in range(len(nums)):
            if nums[i]==1:
                k+=1
            else:
                a.append(k)
                k=0
        a.append(k)
        print(a)
        m=0
        for i in range(len(a)-1):
            if a[i]+a[i+1]>m:
                m=a[i]+a[i+1]
        return m