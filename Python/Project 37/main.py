num = [1,2,0,0]
num.reverse()
k = 34
k_list = [int(i) for i in str(k)]
k_list.reverse()
num_list = []
carry = 0

for i in range(len(num)):
    if i < len(k_list):
        num_sum = num[i] + k_list[i]
        if (num_sum) < 10:
            if carry == 1:
                num_sum = num_sum + 1
                num_list.append(num_sum)
                if (num_sum) >= 10:
                    carry += 1
                else:
                    carry -= 1
            else:
                num_list.append(num_sum)
        elif (num_sum) >= 10:
            carry += 1
            num_list.append(int(str(num_sum)[-1]))

    else:
        num_list.append(num[i])
if carry == 1:
    num_list.append(1)
num_list.reverse()
print(num_list)

