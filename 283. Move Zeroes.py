class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):
            
            print(right)
            if nums[right]!=0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
                

        return nums