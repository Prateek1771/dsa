# https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2026-01-12

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        Ans = 0
        for i in range(1, len(points)):
            Ans += max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1])
            )
        return Ans