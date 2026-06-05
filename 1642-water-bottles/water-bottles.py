class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while True:
            temp = numBottles // numExchange
            if temp >= 1:
                res += temp
                rem = numBottles % numExchange
                numBottles = temp + rem
            else:
                return res
            


        