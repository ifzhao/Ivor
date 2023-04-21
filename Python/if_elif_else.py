print("欢迎来到动物园")
age = int(input("请输入你的年龄："))
vip_level = int(input("请输入你的VIP等级："))
if age < 12:
    print("免费")
elif vip_level > 3:
    print("贵客，免费")
else:
    print("买票")
