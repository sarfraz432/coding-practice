def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            j += 1
            nums[j] = nums[i]
    return j + 1
        
    


nums = []
output = remove_duplicates(nums=nums)
print(nums[:output])
