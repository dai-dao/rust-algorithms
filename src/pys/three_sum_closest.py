
class Solution():
    def threeSumClosest(self, nums, target):
        diff = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                new_diff = abs(target - sum)
                if new_diff < diff:
                    diff = new_diff
                    res = sum
                
                if sum < target:
                    lo += 1
                elif sum > target:
                    hi -= 1
                else: # In case of equal, just return target
                    return target

        return res




print(Solution().threeSumClosest([-1, 2, 1, -4], 1)) # 2
print(Solution().threeSumClosest([0, 0, 0], 1)) # 0
