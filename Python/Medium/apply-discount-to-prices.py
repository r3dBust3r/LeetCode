# Name: apply-discount-to-prices
# URL: https://leetcode.com/problems/apply-discount-to-prices/


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        result = ""
        for w in words:
            if not w[0] == '$':
                result += f"{w} "
                continue

            w = w[1:]
            if w.isdigit():
                price = int(w)
                result += f"${price * (100 - discount) / 100:.2f} "
            else:
                result += f"${w} "

        return result.strip()


print(
    Solution.discountPrices(
        None,
        "1 2 $3 4 $5 $6 7 8$ $9 $10$", 100
    )
)
