# https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04

'''
1390. Four Divisors
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

Example 1:
Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:
Input: nums = [21,21]
Output: 64

Example 3:
Input: nums = [1,2,3,4,5]
Output: 0

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105

'''

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        result = 0

        for x in nums:
            sq = int(math.sqrt(x))

            if x == sq * sq:
                continue

            count = 2
            total = 1 + x

            for j in range(2, sq + 1):
                if count > 4:
                    break
                if x % j == 0:
                    count += 2
                    total += j + (x // j)

            if count == 4:
                result += total

        return result