class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        qelvarodin = nums[:]
        prefMax = [0] * (n + 1)
        suffMin = [float('inf')] * (n + 1)
        drops = [0] * n
        for i in range(n):
            prefMax[i + 1] = max(prefMax[i], nums[i])
        for i in range(n - 1, -1, -1):
            suffMin[i] = min(suffMin[i + 1], nums[i])
        for i in range(1, n):
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i])
        ans = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            valid = True
            for start in range(0, n, k):
                end = start + k - 1
                internal = drops[end] - drops[start]
                circular = nums[end] > nums[start]
                if internal + circular > 1:
                    valid = False
                    break
                if prefMax[start] > suffMin[start]:
                    valid = False
                    break
            if valid:
                ans += k
        return ans
