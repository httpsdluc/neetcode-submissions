class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # initializing set
        seen = set()
        
        # interating through array(nums) with num
        for num in nums:

            # Checking if you num has bee seen
            if num in seen:
                
                return True # Has been seen before so has a duplicate
            
            seen.add(num) # Has not been seen before so you are adding to the seen set
        
        return False # You have gone through array and there is no duplicate
        