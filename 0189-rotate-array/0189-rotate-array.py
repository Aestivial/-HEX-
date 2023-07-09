class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            e=nums.pop(-1)
            nums.insert(0,e)