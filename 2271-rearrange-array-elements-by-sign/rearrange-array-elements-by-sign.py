class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp1 = []
        temp2 = []
        for i in range(n):
            if nums[i] > 0:
                temp1.append(nums[i])
            else:
                temp2.append(nums[i])
        
        j = 0
        for i in range(int(n/2)):
            nums[j] = temp1[i]
            j += 1
            nums[j] = temp2[i]
            j += 1

        return nums
        

        