class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        print('lenth')
        print(len(s))
        print(s[::-1])

        for i in range(len(s)):
            print(roman[s[i]])
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res


romaninput = input('write roman letter: ')

rtoint = Solution()
print(rtoint.romanToInt(romaninput))
