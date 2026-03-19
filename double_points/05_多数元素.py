def majorityElement(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    hashMap = {}
    for i in nums:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1
    for item in hashMap:
        if hashMap[item] > len(nums) / 2:
            return item

def majorityElement2(nums: list[int]) -> int:
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        else:
            if num == candidate:
                count += 1
            else:
                count -= 1

    return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement2(nums))











