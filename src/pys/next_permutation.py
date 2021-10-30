


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i-=1

        if i >= 0:
            j = len(nums) -1
            while nums[j] <= nums[i]:
                j-=1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)


    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1



nums = [1,2,3]
Solution().nextPermutation(nums)
print(nums) # 1,3,2


nums = [3,2,1]
Solution().nextPermutation(nums)
print(nums) # 1,2,3


nums = [1,1,5]
Solution().nextPermutation(nums)
print(nums) # 1,5,1


nums = [1]
Solution().nextPermutation(nums)
print(nums) # 1


nums = [1, 2]
Solution().nextPermutation(nums)
print(nums) # 1, 2