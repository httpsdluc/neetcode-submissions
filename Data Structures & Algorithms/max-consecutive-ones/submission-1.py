class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # input: nums - an array
        # output: return the max num of consecutive 
        # track the max 1s together
        # and track the no. 1
        count_1 = max_count_1 = 0

        # go through array
        for num in nums:
            # if the consequtive 1s end
            if num == 0:
                # check if there is a new max count
                max_count_1 = max(max_count_1, count_1)
                # reset the count of 1s
                count_1 = 0
            else:
                # increment count
                count_1 += 1
        # we have gone through whole nums, return largest count
        return max(max_count_1, count_1)

        