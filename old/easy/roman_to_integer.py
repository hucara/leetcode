class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for idx, c in enumerate(s[::-1]):
            if c == "I":
                if num >= 5:
                    num -= 1
                else:
                    num += 1
            elif c == "V":
                num += 5
            elif c == "X":
                if num >= 50:
                    num -= 10
                else:
                    num += 10
            elif c == "L":
                num += 50
            elif c == "C":
                if num >= 500:
                    num -= 100
                else:
                    num += 100
            elif c == "D":
                num += 500
            elif c == "M":
                num += 1000

        return num
