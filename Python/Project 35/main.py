nums = [3,4,2]
target = 6
num_len = 0
new_len = 0
new = []
new_res = []
final_result = []
final_len = 0
for i in nums:
    num_len += 1

for a in nums:
    for b in range(num_len):
        if (a + nums[b]) != target:
            continue
        elif (a + nums[b]) == target and nums[b] != a:
            new_res.append(a)
            continue
        if a not in new:
            new.append(a)

for b in new:
    new_len += 1
    result = [i for i, x in enumerate(nums) if x == b]
for i in new_res:
    final_len += 1
    final_result.append(nums.index(i))

if final_len >1:
    print(final_result)
elif new_len != 2:
    print(result)
