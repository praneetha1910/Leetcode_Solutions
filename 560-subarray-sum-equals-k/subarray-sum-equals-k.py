from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            ans += freq[prefix - k]
            freq[prefix] += 1

        return ans