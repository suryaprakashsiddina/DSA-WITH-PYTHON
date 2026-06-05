class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        number = "1"
        for i in range(2,n+1):
            res = ""
            count = 1
            curr = number[0]
            for j in range(1,len(number)):
                if curr == number[j]:
                    count += 1
                else:
                    res += str(count) + curr
                    curr = number[j]
                    count = 1
            res += str(count) + curr
            number = res
        return number