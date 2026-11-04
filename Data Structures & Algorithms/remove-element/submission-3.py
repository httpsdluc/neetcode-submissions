class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # input: nums - an int array and val - an int
        # output: k - amount of non-val
        #         nums - altered without val

        # lets go through array and remove the nums that equal val as we get to them
        # once we have gone through whole array get size of array
        # lets overwrite the list

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

