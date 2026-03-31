def jump(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if n == 2:
        return 1
    step = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            step += 1
            current_end = farthest
    return step
# [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
# [2,3,1]
# [3,2,1]
# [1,2]
# [1,1,1,1,1]
# [1,2,1,1,1]
# [2,3,1,1,4]
nums = [3,2,1]
print(jump(nums))

'''
纸面操作记录
测试用例保证都能达到 n-1 处
这里其中就是为了找出一个最短路径 到达 n-1 处
引入一个 step 步长变量代表当前走了多少步
然后再在 step 步长值内引入第二个循环来查找步长内的数能达到的最远距离 
第一个循环应该用while条件控制，当 max >= n-1 时跳出循环
第二个循环结束后，拿到当前步长内的最优距离下标， 当 max 变化的时候执行 step+1 操作



'''


