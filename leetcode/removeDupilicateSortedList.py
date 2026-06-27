def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates in-place from a sorted list and return the new length."""
    if not nums:
        return 0

    write_index = 0
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            write_index += 1
            nums[write_index] = nums[read_index]

    return write_index + 1


if __name__ == "__main__":
    nums = []
    output = remove_duplicates(nums)
    print(nums[:output])
