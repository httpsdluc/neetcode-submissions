class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # looking through array starting at nums[0] to the end variable
        for i in range (len(nums)):
            # looking at number next to current from nums[1] to the end variable
            for j in range (i + 1, len(nums)):
                # check i and j in nums against each other 
                if nums[i]==nums[j]:
                    return True
        return False

        