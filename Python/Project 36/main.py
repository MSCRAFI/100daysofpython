nums = [4, 2, 3, 5]
target = 6
new1 = []
new2 = []
result = []


def funcNew1():
    for i in range(len(nums)):
        if new1[0] == nums[i]:
            result.append(i)


def funcNew2():
    for i in new2:
        for a in new2:
            if (i + a) == target:
                result.append(nums.index(i))


for i in range(len(nums)):
    alt_target = target - nums[i]
    if nums[i] == alt_target:
        new1.append(nums[i])
    elif nums[i] != alt_target:
        new2.append(nums[i])
if len(new1) >= 2:
    funcNew1()
elif len(new2) >= 2:
    funcNew2()

print(result)
