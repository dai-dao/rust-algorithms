# defaultdict don't have to initialize every key, it does for you
from collections import defaultdict


class Solution:
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1
        
        for n in note:
            if letters[n] <= 0:
                return False
            letters[n] -= 1

        return True





print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
