# 리트코드 238
# 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

nums = [1, 2, 3, 4]

def ProductArray(nums):
    result = []
    tmp = 1
    for i in range(len(nums)):
        result.append(tmp)
        tmp = tmp * nums[i]
    print(result)

    tmp = 1
    for i in range(len(nums)-1, 0-1, -1):
        result[i] = result[i] * tmp
        print(result)
        tmp = tmp * nums[i]
        print(tmp)

    return result

print(ProductArray(nums))