class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        k=[]
        i=0
        while i<len(nums):
            start=nums[i]
            while i<len(nums)-1 and nums[i+1]==nums[i]+1:
                i+=1
            stop=nums[i]
            if start==stop:
                k.append(str(start))
            else:
                k.append(str(start)+"->"+str(stop))
            i+=1
        return k