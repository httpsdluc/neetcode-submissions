class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # input: nums - an array of ints
        # output: the max num of consecutive 1

        # track current consec 1s and max count
        count_1 = 0
        max_count = 0

        # we go through the array, 
        # if we see 1, we have started 1 count
        # if we see 0 we restart the count_1
        
        for num in nums:
            if num == 1:
                count_1 += 1
            if count_1 >= max_count:
                    max_count = count_1
                    
            if num == 0:
                count_1 = 0
            
        return max_count