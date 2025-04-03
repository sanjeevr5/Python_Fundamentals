def three_sum(nums):
    nums.sort()
    index: int = 0
    leng: int = len(nums)
    outputs: list[list[int]] = []
    while index < leng - 2:
        while index and index < leng - 2 and nums[index - 1] == nums[index]:
            index += 1
        left: int = index + 1
        right: int = leng - 1
        while left < right:
            if (tot := nums[index] + nums[left] + nums[right]) == 0:
                outputs.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1
                while left <= right and nums[left - 1] == nums[left]:
                    left += 1
                while left <= right and nums[right + 1] == nums[right]:
                    right -= 1
            elif tot < 0:
                left += 1
            else:
                right -= 1
        index += 1
    return outputs


assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([1, 2, 3]) == []