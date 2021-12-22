

# литкод задачи
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if i == val:
                nums[0], nums[i] = nums[i], nums[0]
        print(val, nums)


t = Solution.removeElement([3, 2, 2, 3], 2)

# 35. Search Insert Position
class Solution:

    def searchInsert(nums: list[int], target: int):
        if target in nums:
            print(nums.index(target))

        else:
            nums.append(target)
            print(sorted(nums).index(target))


Solution.searchInsert([1, 3, 5, 6, 10, 13, 20], 9)


# 66. Plus One
class Solution:

    def plusOne(digits: list[int]):
        a = int(''.join(map(str, digits))) + 1
        new_list = []
        for i in str(a):
            new_list.append(int(i))
        print(new_list)


Solution.plusOne([1, 2, 3])
