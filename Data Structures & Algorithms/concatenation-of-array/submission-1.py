class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenNum = len(nums)
        for i in range(lenNum):
            nums.append(nums[i])

        return nums