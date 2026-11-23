class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums - an array containing 0s and 1s
        # return the max num of consecutive 1s

        # we need to track current 1s
        count1 = 0
        # max num of 1s
        max_count1 = 0

        # we need to go through the array
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                count1 = 0
            
            if max_count1 < count1:
                max_count1 = count1
        return max_count1
            

        