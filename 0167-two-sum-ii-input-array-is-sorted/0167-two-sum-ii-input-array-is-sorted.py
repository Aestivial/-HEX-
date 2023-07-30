class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,x in enumerate(numbers):
            if target-x not in d:
                d[x]=i
            else:
                return [d[target-x]+1,i+1]