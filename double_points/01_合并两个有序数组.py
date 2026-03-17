def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        nums1[:] = nums2
        return
    elif n == 0:
        return
    l1 = 0
    l2 = 0
    result = []
    for index in range(m + n):
        if l1 <= m-1 and l2 <= n-1:
            if nums1[l1] <= nums2[l2]:
                result.append(nums1[l1])
                l1 += 1
            else:
                result.append(nums2[l2])
                l2 += 1
        elif l1 <= m-1:
                result.append(nums1[l1])
                l1 += 1
        elif l2 <= n-1:
                result.append(nums2[l2])
                l2 += 1
    nums1[:] = result
    print(nums1)

def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        nums1[:] = nums2
        return
    elif n == 0:
        return
    l1 = m - 1
    l2 = n - 1

    while l1 >= 0 or l2 >= 0:
        if l1 >= 0 and l2 >= 0:
            if nums1[l1] >= nums2[l2]:
                nums1[l1+l2+1] = nums1[l1]
                l1 -= 1
            else:
                nums1[l1+l2+1] = nums2[l2]
                l2 -= 1
        elif l1 >= 0:
            nums1[l1+l2+1] = nums1[l1]
            l1 -= 1
        else:
            nums1[l1+l2+1] = nums2[l2]
            l2 -= 1
    print(nums1)

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge2(nums1, 3, nums2, 3)
# print(nums1)







