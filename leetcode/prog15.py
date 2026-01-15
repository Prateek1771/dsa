# leetcode.com/problems/maximize-area-of-square-hole-in-grid/?envType=daily-question&envId=2026-01-15

class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        hBars.sort()
        vBars.sort()

        maxiH, maxiV, maxi = 1, 1, 1

        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i-1] == 1:
                maxi += 1
            else:
                maxiH = max(maxiH, maxi)
                maxi = 1
        maxiH = max(maxiH, maxi)

        maxi = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i-1] == 1:
                maxi += 1
            else:
                maxiV = max(maxiV, maxi)
                maxi = 1
        maxiV = max(maxiV, maxi)

        side = min(maxiH+1, maxiV+1)
        return side * side