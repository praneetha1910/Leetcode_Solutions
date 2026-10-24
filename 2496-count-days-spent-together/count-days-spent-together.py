
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a = max(arriveAlice, arriveBob)
        b = min(leaveAlice, leaveBob)
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        start = sum(days[:int(a[:2]) - 1]) + int(a[3:])
        end = sum(days[:int(b[:2]) - 1]) + int(b[3:])
        return max(0, end - start + 1)
