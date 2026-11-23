class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # input:
        # nums - an integer array
        # val - an integer we are trying to remove

        # output:
        # the number of elements in nums not equal to val

        # we iterate through the array, if the nums[index] == val, we remove it in place
        # once we are done removing all of them, we return size
        # k tracks how many non val there are and help rewrite nums
        k = 0
        # were reading the array with i
        for i in range(len(nums)):
            # if num[i] is not equal to val
            if nums[i] != val:
                # writes to the next clean slot
                nums[k] = nums[i]
                k += 1
        return k