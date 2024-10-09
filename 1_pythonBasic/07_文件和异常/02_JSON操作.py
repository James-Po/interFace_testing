import json
with open("我的名字.json", encoding="utf-8") as f:
    data = json.load(f)
    print(type(data))
    print(data)

    #name
    print(data["name"])
    print(data.get("name"))