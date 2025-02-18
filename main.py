class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        length=len(nums) 
        hash = {}
        
        for i in range(length):
            hash[nums[i]] = i

        for i in range(length):
            remains = target - nums[i]
            if remains in hash and hash[remains] != i:
                return [i, hash[remains]]

        return []








