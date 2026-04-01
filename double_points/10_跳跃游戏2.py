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
再引入一个 current_end 表示当前步数最长的距离
再引入一个 farthest 最长步表示滑动序列最长的距离



'''


