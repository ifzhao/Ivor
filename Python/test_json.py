import json
a = {
    "name": "测试",
    "int1": 12241816,
    "h": {
        "h1": 180,
        "h2": 190
    }


}

b = json.dumps(a)
print(b)
# f2 = open('one_json.json', "a")
# f2.write(b)
# f2.close()
