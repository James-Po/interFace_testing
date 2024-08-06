"""
append()添加数据
列表.append(数据)  # 想列表的尾部添加数据
# 返回: None, 所以不用使用 变量 = 列表.append()
直接在原列表中添加数据, 不会生成新的列表,如果想要查看添加后的数据, 直接 print() 打印原列表
"""
"""
表.pop(index)   
# 根据下标删除列表中的数据
- index 下标可以不写, 默认删除在最后一个
- 返回, 删除的数据
"""
# 定义一个空列表
list1 = []

print(list1)

# 添加数据 张三
list1.append('张三')
print(list1)
list1.append('李四')
print(list1)
list1.append('王五')
list1.append('马六')
print(list1)

# 删除最后一个数据
list1.pop()
print(list1)

# 删除第二个数据
name = list1.pop(1)
print('删除的对象为：', name)
print(list1)


print('--------------------------------------')
"""
想要修改列表中的数据, 直接是所有下标即可
列表[下标] = 新数据
"""
my_list = [1, 2]
print(my_list)
my_list[0] = 10
print(my_list)

my_list[-1] = 200
print(my_list)