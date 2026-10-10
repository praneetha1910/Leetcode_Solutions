from typing import List
import heapq

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(diff)

        for i in range(n - 1):
            cost = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= cost:
                k -= cost
            else:
                q, r = divmod(k, i + 1)
                for j in range(i + 1):
                    diff[j] = diff[i] - q - (1 if j < r else 0)
                k = 0
                break

            if i == n - 2:
                diff[-2] = max(0, diff[-2] - k)
                k = 0

        return sum(x * x for x in diff[:-1])