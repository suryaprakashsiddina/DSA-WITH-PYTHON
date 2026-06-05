class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = []
        for i in range(len(nums)):
            count = 0
            if nums[i] not in unique:
                unique.append(nums[i])
                for j in range(i, len(nums)):
                    if nums[i] == nums[j]:
                        count += 1
                
                if count == 1:
                    return nums[i]
        