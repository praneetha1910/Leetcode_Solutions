class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=10
        alice=True
        while n>=turn:
            n-=turn
            turn-=1
            alice=not alice
        return not alice
        