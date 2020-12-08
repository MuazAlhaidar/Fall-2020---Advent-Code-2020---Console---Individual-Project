def twoSum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]], i]
        else:
            required[nums[i]] = i


def multiplyTwoSum(nums, arr):
    return nums[arr[0]] * nums[arr[1]]


def threeSum(nums, target):
    required = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (target - (nums[i] + nums[j])) in required:
                return [required[target - (nums[i] + nums[j])], i, j]
        required[nums[i]] = i


def multiplyThreeSum(nums, arr):
    return nums[arr[0]] * nums[arr[1]] * nums[arr[2]]


def getInput():
    f = open("input.txt")
    stringList = f.read().split()
    fileInput = []
    for x in range(len(stringList)):
        fileInput.append(int(stringList[x], base=10))
    return fileInput


numberSet = getInput()

target = 2020

print(multiplyTwoSum(numberSet, twoSum(numberSet, target)))
print(multiplyThreeSum(numberSet, threeSum(numberSet, target)))
