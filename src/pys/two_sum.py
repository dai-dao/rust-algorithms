class Solution(object):
    def twoSum(self, nums, target):
        vals = {}
        for i, n in enumerate(nums):
            if target - n in vals:
                return [i, vals[target-n]]
            vals[n] = i
        return []




print(Solution().twoSum([2, 7, 11, 15], 18))