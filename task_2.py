"""[LeetCode] There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number
 of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies."""


class Solution:
    def __init__(self, candies: list[int]) -> None:
        self.candies = candies

    def kids_with_candies(self, extra_candies: int) -> list[bool]:

        max_item = max(self.candies)
        bool_list = []
        for item in self.candies:
            if item + extra_candies >= max_item:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list


if __name__ == '__main__':
    candies_list = [4, 2, 1, 1, 2]
    s = Solution(candies=candies_list)
    print(s.kids_with_candies(extra_candies=1))
