

class Solution:
    def permute(self, arr):
        return self._permute(arr)

    def _permute(self, arr, perm=[]):
        res = []
        if not arr:
            return [perm]
        for i in range(len(arr)):
            res += self._permute(arr[:i] + arr[i+1:], perm + [arr[i]])
        return res

    def permuteIterative(self, arr):
        results = []
        stack = [(arr, [])]
        while len(stack):
            nums, perm = stack.pop()
            if not nums:
                results.append(perm)
                continue
            for i in range(len(nums)):
                stack.append((nums[:i] + nums[i+1:], perm + [nums[i]]))
        return results



print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

# print(Solution().permute2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permuteIterative([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
