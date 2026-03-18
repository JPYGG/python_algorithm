def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n

    slow = 2

    for fast in range(2, n):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    del nums[slow:]
    return slow

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
print(nums)














