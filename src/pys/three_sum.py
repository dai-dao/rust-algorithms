
class Solution:

    def threeSum(self, nums):
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            seen = set()
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen:
                    # needs to sort to be identically hashable
                    res.add(tuple(sorted((val1, val2, complement))))
                seen.add(val2)
        return res


    def threeSumI(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # Make sure skip duplicates
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res


    def twoSum(self, nums, i, res):
        seen = set()
        j = i+1
        while j < len(nums):
            complement = -nums[j] - nums[i]

            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1

            seen.add(nums[j])
            j += 1


    # Only works for sorted approach
    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi) :
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # do some more skipping in case of repeating lo values
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1



print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([])) # []
print(Solution().threeSum([0])) # []