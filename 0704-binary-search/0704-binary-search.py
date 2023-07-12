class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bins(arr,start,end,target):
            if start>end:
                return -1
            mid=(start+end)//2
            if arr[mid]>target:
                return bins(arr,start,mid-1,target)
            elif arr[mid]<target:
                return bins(arr,mid+1,end,target)
            else:
                return mid
        
        return bins(nums,0,len(nums)-1,target)