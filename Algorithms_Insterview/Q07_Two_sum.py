#리트코드 1
nums = [2, 7, 11, 15]
target = 18

def twoSum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum(nums))