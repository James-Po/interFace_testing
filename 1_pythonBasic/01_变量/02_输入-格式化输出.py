# 创建变量，接收你的名字跟年龄
name = input("请输入你的名字：")
age = input("请输入你的年龄")
sex = '男'

print("我的名字叫：" + name)

print(type(name), name)

# 格式化输出 1
print(f'我的名字叫{name}，我今年{age}岁，我是{sex}的')

# 格式化输出 1
print('My name is {},I am {} years old, I am a {}'.format(name, age, sex))