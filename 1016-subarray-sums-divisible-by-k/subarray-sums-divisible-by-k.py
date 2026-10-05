from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            ans += freq[rem]
            freq[rem] += 1

        return ans