class Solution(object):
    def findNumbers(self, nums):
        e=0
        for i in nums:
            if len(str(i))%2==0:
                e+=1
        return e