class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_sets=[[]]
        for num in nums:
            power_sets+=[subset+[num] for subset in power_sets]
        return power_sets