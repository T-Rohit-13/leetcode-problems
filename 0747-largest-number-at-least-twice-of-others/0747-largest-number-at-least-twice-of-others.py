class Solution(object):
    def dominantIndex(self, nums):
        maxi=max(nums)
        for i in nums:
            if i ==maxi:
                continue
            ind=nums.index(maxi)
            if (i*2)>maxi:
                return -1
        return ind
               
        