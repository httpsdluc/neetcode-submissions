class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # input: nums - an array
        # output: return the max num of consecutive 
        # track the max 1s together
        count_1 = max_count_1 = 0

        # go through array
        for num in nums:
            if num == 0:
                max_count_1 = max(max_count_1, count_1)
                count_1 = 0
            else:
                count_1 += 1
        return max(max_count_1, count_1)

        