def rotate(nums: list[int], k: int) -> None:

    if k > len(nums):
        k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def rotate2(nums: list[int], k: int) -> None:

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(0, len(nums) - 1)
    reverse(k, len(nums) - 1)
    reverse(0, k - 1)
    print(nums)
nums = [1,2,3,4,5,6,7]
k = 3
rotate2(nums, k)











