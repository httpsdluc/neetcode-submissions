class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums - integer array
        # val - integer

        # output
        # - remove the occurrences of val in nums
        # after nums has been removed, what is length of nums after

        # we can sort the array, this way vals in the array can be grouped together
        # we can delete val from nums


        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k