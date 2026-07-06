class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        co=0
        nums.append(0)
        col=[]
        for i in nums:
            if i==1:
                co+=1
            else:
                col.append(co)
                co=0
        return max(col)
        