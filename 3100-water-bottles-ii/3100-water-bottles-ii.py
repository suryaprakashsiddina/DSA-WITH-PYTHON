class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty_bottles = res
        numBottles = 0 #drunk
        while True:
            prev_empty_bottles = empty_bottles
            empty_bottles = empty_bottles - numExchange
            if empty_bottles >= 0:
                res += 1
                numBottles += 1
                numExchange += 1
            else:
                if numBottles:
                    empty_bottles = prev_empty_bottles
                    empty_bottles += numBottles
                    numBottles = 0
                else:
                    return res
                    
            if empty_bottles == 0:
                empty_bottles = numBottles
                numBottles = 0       