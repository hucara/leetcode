class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        dot_number = ""
        str_number = str(n)
        for idx, c in enumerate(str_number[::-1]):
            if (idx + 1) % 3 == 0 and (idx + 1) < len(str_number):
                dot_number = "." + c + dot_number
            else:
                dot_number = c + dot_number

        return dot_number
