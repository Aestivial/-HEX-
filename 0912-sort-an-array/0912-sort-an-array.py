class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            mid=len(nums)//2
            L=nums[:mid]
            R=nums[mid:]
            self.sortArray(L)
            self.sortArray(R)
            
            i=j=k=0
            r_len=len(R)
            l_len=len(L)
            
            while i<l_len and j<r_len:
                if L[i]<R[j]:
                    nums[k]=L[i]
                    i+=1
                else:
                    nums[k]=R[j]
                    j+=1
                k+=1
            while i<l_len:
                nums[k]=L[i]
                i+=1
                k+=1
            while j<r_len:
                nums[k]=R[j]
                j+=1
                k+=1
            return nums