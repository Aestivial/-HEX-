class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        if target not in nums:
            if target>nums[len(nums)-1]:
                return len(nums)
            for i in nums:
                if i<target:
                    k+=1
            return k
        else:               
            return nums.index(target)