from random import choice

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.idx_map = dict()
    def insert(self, val: int) -> bool:
        if val not in self.idx_map:
            self.nums.append(val)
            self.idx_map[val] = len(self.nums) - 1
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            idx = self.idx_map[val]
            last_num = self.nums[-1]
            self.nums[idx] = last_num
            self.idx_map[last_num] = idx
            self.nums.pop()
            del self.idx_map[val]
            return True
        return False
    def getRandom(self) -> int:
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


'''
数组的插入和查询为O(1)，删除为O(n)，尾删为O(1)


'''
