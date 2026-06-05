class Solution:
    def generate_rows(self,row: int) -> List[int]:
        res = 1
        ans = [1]
        
        for col in range(1,row):
            res = res * (row - col)
            res = res // col
            ans.append(res)
        return ans

    def generate(self, n: int) -> List[List[int]]:
        ans = []

        for i in range(1,n+1):
            ans.append(self.generate_rows(i))
        return ans
        