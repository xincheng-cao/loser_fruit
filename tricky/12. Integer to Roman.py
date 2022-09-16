class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        '''
        ans=''
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        for e in VALUE_SYMBOLS:
            val,sym=e
            while num>=val:
                num-=val
                ans+=sym
        return ans





