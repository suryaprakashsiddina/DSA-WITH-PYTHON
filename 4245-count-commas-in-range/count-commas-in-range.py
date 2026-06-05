class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        base = 1000
        
        while base <= n:
            end = min(n, base * 1000 - 1)
            
            # digits in base
            digits = len(str(base))
            commas = digits // 3
            
            count = end - base + 1
            total += count * commas
            
            base *= 1000
        
        return total
        
        