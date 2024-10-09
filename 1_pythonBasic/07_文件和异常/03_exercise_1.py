"""
1. 先定义 info.json 文件
我叫小明,我今年 18 岁,性别男, 爱好 听歌, 吃饭,打豆豆,
我的居住地址为 国家中国, 城市广州.   ---> 对象

我叫小红,我今年 17 岁,性别女, 爱好 听歌, 学习,购物
我的居住地址为 国家 中国, 城市北京.   ---> 对象
-----
2. 使用 Python 代码 读取 每个人的姓名, 年龄 性别, 城市
"""
import json
with open("info.json", encoding="utf-8") as f:
    data = json.load(f)
    for d in data:
        sex = '男' if d.get('isMan') else '女'
        print(f"name : {d.get('name')}, age : {d.get('age')}, "
              f"sex : {d.get('sex')}, city : {d.get('address').get('city')}")