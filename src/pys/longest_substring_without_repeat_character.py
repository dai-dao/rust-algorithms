from collections import defaultdict


class Solution:
    # Brute force: Check all substring one by one to see if it has no duplicate character
    # def lengthOfLongestSubstring(self, s):
    #     def check(start, end):
    #         chars = defaultdict(int)
    #         for i in range(start, end+1):
    #             c = s[i]
    #             chars[c] += 1
    #             if chars[c] > 1:
    #                 return False
    #         return True
    #     res = 0
    #     n = len(s)
    #     for i in range(n):
    #         for j in range(i, n):
    #             if check(i, j):
    #                 res = max(res, j-i + 1)
    #     return res

    # v2
    # def lengthOfLongestSubstring(self, s):
    #     res = 0
    #     n = len(s)
    #     for i in range(n):
    #         chars = defaultdict(int)
    #         for j in range(i, n):
    #             c = s[j]
    #             chars[c] += 1
    #             if chars[c] == 1:
    #                 res = max(res, j-i + 1)
    #             else:
    #                 break
    #     return res

    # v3: sliding window
    # Move start up until end no longer contains duplicates, and keep moving end until
    # string length
    # def lengthOfLongestSubstring(self, s):
    #     res = 0
    #     start = 0
    #     end = 0
    #     chars = defaultdict(int)
    #     while end < len(s):
    #         chars[s[end]] += 1

    #         while chars[s[end]] > 1:
    #             chars[s[start]] -= 1
    #             start += 1

    #         res = max(res, end - start + 1)
    #         end += 1

    #     return res


    # v4: optimized sliding window, from O(2n) to O(n)
    def lengthOfLongestSubstring(self, s):
        res = 0
        start = 0
        chars = {}

        for i in range(len(s)):
            # this part, don't have to move start little by little, can just skip
            # straight to the part without duplicate
            # print("start", start, "i", i, 'new res', i - start + 1, 'res', res)

            if s[i] in chars:
                # start should only be moved forward, not backwards
                if chars[s[i]] >= start:
                    start = chars[s[i]] + 1
            res = max(res, i - start + 1)
            chars[s[i]] = i

        return res


# int[26] for Letters 'a' - 'z' or 'A' - 'Z'
# int[128] for ASCII


print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("")) # 0
print(Solution().lengthOfLongestSubstring("abba")) # 2
print(Solution().lengthOfLongestSubstring("tmmzuxt")) # 5
