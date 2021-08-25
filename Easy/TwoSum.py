class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,num  in enumerate(nums):
            rem = target-num
            if rem in d:
                return [d[rem],index]
            else:
                d[num] = index
#Runtime: 52 ms, faster than 96.11% of Python3 online submissions for Two Sum.
