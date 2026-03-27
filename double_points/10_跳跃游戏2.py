def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    max_reach = 0
    step = 0
    for i in range(n):
        if i + nums[i] >= max_reach:
            max_reach = max(max_reach, i + nums[i])
            step += 1
        if max_reach >= n - 1:
            return step
    return step

# [1,2,1,1,1]
nums = [2,3,1,1,4]
print(jump(nums))




