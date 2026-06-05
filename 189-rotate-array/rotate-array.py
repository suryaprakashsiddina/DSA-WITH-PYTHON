class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            print("Array is empty. so cant perform rotation")
        else:
            k = k % len(nums) # Optimize for large rotations
            for i in range(k):
                temp = nums.pop()
                nums.insert(0,temp)

        