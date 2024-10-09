import json
with open("我的名字.json", encoding="utf-8") as f:
    data = json.load(f)
    print(type(data))
    print(data)

    #name
    print(data["name"])
    print(data.get("name"))

    # age
    print(data["age"])
    print(data.get("age"))

    # 取出第一个爱好
    print(data["hobby"][0])
    print(data.get("hobby")[0])

    # 取出国家
    print(data["address"]["country"])
    print(data.get("address").get("country"))