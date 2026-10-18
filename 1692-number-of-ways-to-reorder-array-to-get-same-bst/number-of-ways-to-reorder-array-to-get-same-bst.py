
from math import comb
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        def solve(arr):
            if len(arr) <= 2:
                return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            ways = comb(len(arr) - 1, len(left))
            ways *= solve(left)
            ways *= solve(right)

            return ways % MOD

        return (solve(nums) - 1) % MOD
