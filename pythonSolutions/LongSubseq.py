import numpy as np

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = np.ones((len(nums)),dtype=int)
        for i in range(1,len(nums)):
            maxi = 1
            for j in range(i-1, -1,-1):
                if(nums[i]>nums[j]):
                    arr[i] = max(arr[i], arr[j]+1)
        print(arr)
        ans = np.max(arr)
        return ans

s = Solution()
nums = [0,1,0,3,2,3]
s.lengthOfLIS(nums)

