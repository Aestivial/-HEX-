class Solution:                  
    def subsets(self, nums: List[int]) -> List[List[int]]:       
        ans=[]
        n=len(nums)
        def solve(arr,index,subset):
            if index==n:
                ans.append(subset)
                return
            solve(arr,index+1,subset)
            solve(arr,index+1,subset+[arr[index]])
        solve(nums,0,[])
        return ans