# https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05

'''
1975. Maximum Matrix Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
'''

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        totalSum = 0
        neg = 0
        minAbs = float('inf')

        for row in matrix:
            for v in row:
                if v < 0:
                    neg += 1
                av = abs(v)
                totalSum += av
                minAbs = min(minAbs, av)

        return totalSum if neg % 2 == 0 else totalSum - 2 * minAbs