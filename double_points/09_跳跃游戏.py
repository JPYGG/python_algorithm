def canJump(nums: list[int]) -> bool:
    n = len(nums)
    if nums[0] == 0 and n > 1:
        return False
    if n == 1:
        return True
    v = 0
    for i in range(0, n):
        if v < 0:
            return False
        if nums[i] > 0:
            v = max(v, nums[i])
            if v >= n - i - 1:
                return True
            else:
                v -= 1
        else:
            v -= 1
    return False

def canJump2(nums: list[int]) -> bool:
    n = len(nums)
    max_reach = 0

    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True

    return False

# [3,2,1,0,4]
# [2,3,1,1,4]
# nums = [1, 0, 1, 0]
nums = [1,1,1,0]
print(canJump(nums))
