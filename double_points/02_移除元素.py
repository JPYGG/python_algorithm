def removeElement(nums: list[int], val: int) -> int:
    k = 0
    result = []
    for item in range(len(nums)):
        if nums[item] != val:
            k += 1
            result.append(nums[item])
    nums[:] = result
    return k

def removeElement2(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    # print(nums)
    return slow

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement2(nums, val))


