class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = r = 0
        for n in nums:
            if n == 1:
                c += 1
                r = max(r, c)
            else:
                c = 0
        return r
