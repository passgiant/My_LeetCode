class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li = []
        for i, j in enumerate(nums):
            x = j
            for k, l in enumerate(nums):
                if x + l == target and i != k:
                    li.append(i)
                    li.append(k)
                    return li