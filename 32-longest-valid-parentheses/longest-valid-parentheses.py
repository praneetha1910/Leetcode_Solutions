class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        max_len = 0

        for i in range(1, len(s)):
            if s[i] == ')':

                if s[i - 1] == '(':
                    dp[i] = 2
                    if i >= 2:
                        dp[i] += dp[i - 2]

                else:
                    prev = dp[i - 1]
                    j = i - prev - 1

                    if j >= 0 and s[j] == '(':
                        dp[i] = prev + 2

                        if j > 0:
                            dp[i] += dp[j - 1]

            max_len = max(max_len, dp[i])

        return max_len