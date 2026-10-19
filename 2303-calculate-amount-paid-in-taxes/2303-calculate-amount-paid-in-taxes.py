class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        res = 0
        prev = 0
        skip = False
        for i, bracket in enumerate(brackets):
            if skip:
                continue
            if income <= bracket[0]:
                res += (income - prev) * bracket[1]*0.01
                skip = True
                continue
            res += (bracket[0] - prev) * bracket[1]*0.01
            prev = bracket[0]
             
        return res