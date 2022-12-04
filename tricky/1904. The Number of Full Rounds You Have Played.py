import math


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start_hr = int(loginTime[:2])
        start_mn = int(loginTime[3:])

        end_hr = int(logoutTime[:2])
        end_mm = int(logoutTime[3:])

        night = False
        if start_hr > end_hr:
            night = True
        elif start_hr == end_hr:
            if start_mn > end_mm:
                night = True

        if not night:
            start = 60 * start_hr + start_mn
            start = math.ceil(start / 15)
            end = math.floor((60 * end_hr + end_mm) / 15)

        else:
            start = 60 * start_hr + start_mn
            start = math.ceil(start / 15)
            end = math.floor((60 * end_hr + end_mm) / 15) + 24 * 4
        if end - start < 0:
            return 0
        else:
            return end - start
