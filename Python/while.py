import random
nums = random.randint(1, 100)
flag = True
i = 0
num = 0
while flag:
    guess_num = int(input("请输入你猜测的数据"))
    i += 1
    if guess_num == nums:
        print("猜中了")
        flag = False
    else:
        if guess_num > nums:
            print("猜测大了")
        else:
            print("猜测小了")
print(f"你总共猜测了{i}次")