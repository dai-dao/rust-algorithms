class Solution:
    def threeSumSmaller(self, nums, target):
        sorted(nums)
        sum = 0
        for i in range(len(nums) - 2):
            sum += self.twoSumSmaller(nums, i+1, target - nums[i])

        return sum

    def twoSumSmaller(self, nums, start, target):
        left = start
        right = len(nums) - 1
        sum = 0
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                # Everything in between will sum to less than target
                # Move left to right and keep searching
                sum += right - left
                left += 1
        return sum


print(Solution().threeSumSmaller([-2, 0, 1, 3], 2)) # 2
print(Solution().threeSumSmaller([], 2)) # 0
print(Solution().threeSumSmaller([0], 2)) # 0
