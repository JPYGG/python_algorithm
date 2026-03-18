def removeDuplicates(nums: list[int]) -> int:

    slow = 0
    k = 0
    while slow < len(nums):
        fast = slow + 1
        while fast < len(nums) and nums[fast] == nums[slow]:
            fast += 1
        nums[k] = nums[slow]
        k += 1
        slow = fast

    return k

def removeDuplicates2(nums: list[int]) -> int:

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

def removeDuplicates3(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    slow = 1

    for fast in range(1, n):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    nums[:] = nums[:slow]
    return slow

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates3(nums))
print(nums)




