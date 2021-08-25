class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[x]] for x in range(len(nums))]
      
#Runtime: 116 ms, faster than 90.12% of Python3 online submissions for Build Array from Permutation.
#Memory Usage: 14.3 MB, less than 89.82% of Python3 online submissions for Build Array from Permutation.
