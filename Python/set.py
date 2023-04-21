# 定义集合
my_set = {'卡卡西','空','莹','卡卡西','空','莹','卡卡西','空','莹'}
my_set_empty = set()
print(f'my_set的内容为{my_set},数据类型是{type(my_set)}')
print(f'my_set_empty的内容为{my_set_empty},数据类型是{type(my_set_empty)}')

# 增加元素
my_set.add('凝光')
print(f'my_set增加内容后的结果是{my_set}')

# 移除元素
my_set.remove('卡卡西')
print(f'my_set移除元素后的结果是{my_set}')

# 随机取出一个元素
element = my_set.pop()
print(f'my_set随机取出一个元素，取出的元素是{element},取出后的my_set为{my_set}')

# 清空集合
my_set.clear()
print(f'清空后的集合是{my_set}')

# 取两个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
set3 = set1.difference(set2)
print(f'取差集的结果为{set3}')

# 消除两个集合的交集
set1 = {1,2,3}
set2 = {1,4,5}
set1.difference_update(set2)
print(f'消除交集后的结果为{set1}')

# 合并集合
set1 = {1,2,3}
set2 = {1,4,5}
set3 = set1.union(set2)
print(f'{set3}')

# 统计集合的元素个数
num = len(set3)
print(f'{num}')

# 集合的遍历
# 集合没有下标索引，不能用while循环
for element in set3:
    print(f'{element}')

