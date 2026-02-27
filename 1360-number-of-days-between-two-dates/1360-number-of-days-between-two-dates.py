class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def is_leap(y: int) -> bool:
            return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

        def date(date: str) -> int:
            date = date.split('-')
            y = int(date[0])
            m = int(date[1])
            d = int(date[2])

            days = 0

            for x in range(1900, y):
                days += 365
                days += 1 if is_leap(x) else 0

            for x in range(1, m):
                days += 31
                days -= 1 if x == 4 or x == 6 or x == 9 or x == 11 else 0
                if x == 2:
                    days -= 2 if is_leap(y) else 3

            days += d
            return days

        return abs(date(date1) - date(date2))

        


