class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cnt1 , cnt2 = 0,0
        ele1 , ele2 = float('-inf'), float('-inf')

        for i in range(n):
            if cnt1 == 0 and ele2 != arr[i]:
                cnt1 = 1
                ele1 = arr[i]
            elif cnt2 == 0 and ele1 != arr[i]:
                cnt2 = 1
                ele2 = arr[i]
            elif ele1 == arr[i]:
                cnt1 += 1
            elif ele2 == arr[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        ls = []
        cnt1 , cnt2 = 0, 0
        for i in range(n):
            if ele1 == arr[i]:
                cnt1 += 1
            if ele2 == arr[i]:
                cnt2 += 1
        mini = int(n/3)+1
        if cnt1 >= mini:
            ls.append(ele1)
        if cnt2 >= mini:
            ls.append(ele2)
        
        return ls
        