# Name: maximum-number-of-balloons
# URL: https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c == 'b': balloons['b'] += 1
            if c == 'a': balloons['a'] += 1
            if c == 'l': balloons['l'] += 1
            if c == 'o': balloons['o'] += 1
            if c == 'n': balloons['n'] += 1

        balloons['l'] = balloons['l'] // 2
        balloons['o'] = balloons['o'] // 2

        return min([v for _,v in balloons.items()])


print(
    Solution.maxNumberOfBalloons(
        None,
        "looonaoonoooonbbbllalxballpoon"
    )
)
