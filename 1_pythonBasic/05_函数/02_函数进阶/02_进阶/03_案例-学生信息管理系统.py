# 定义一个列表，保存所有学生信息
stu_list = [{'name' : 'amy', 'age' : 11}, {'name' : 'bob', 'age' : 22}, {'name' : 'alice', 'age' : 33}]


# 录入学生信息
def make_student():
    # 录入单个学生信息
    name = input('please enter your name: ')
    age = input('please enter your age: ')
    # 将学生信息录入字典
    stu_dict = {'name' : name, 'age' : age}
    # 返回单个学生信息
    print(stu_dict)
    return stu_dict


# 展示学生信息
def show_stu_info():
    print('----------Students information----------')
    j = 1  # 初始序号
    for stu_dict in stu_list:
        print(f'{j}. {stu_dict["name"]}: {stu_dict["age"]}')
        j += 1      # 序号自增
    print('----------------------------------------')


if __name__ == '__main__':

    make_student()
    show_stu_info()
