"""[LeetCode] Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution,
 and you may not use the same element twice. You can return the answer in any order."""


class Solution:

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def two_sum(self, target: int) -> list[int]:
        nums_dict = {}
        for i, n in enumerate(self.nums):
            if n in nums_dict:
                return [nums_dict[n], i]

            else:
                nums_dict[target - n] = i


if __name__ == '__main__':
    s = Solution(nums=[2, 5, 5, 11])
    result = s.two_sum(target=10)
    print(result)
