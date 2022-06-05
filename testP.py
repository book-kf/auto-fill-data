import re
from audioop import reverse

def getOpenFlatformData(data: str) -> list:

    data = data.splitlines()
    print(len(data))
    data.reverse()

    allParameters: list = []

    # s = '    field05: Optional[str] = Field(title="字段5",max_length=18, description="预留字段5", default=\'\')'
    for s in data:
        s = s.strip()
        match = re.match("class", s)  # 字段名称
        if match:
            continue
        elif s.find("=") >= 0:

            dic = {}
            match = re.search("(.*):", s)  # 字段名称
            dic['name'] = match.group(1)

            match = re.search("Optional\[(.*?)\]", s)  # 是否必填，匹配到可选，没匹配到必填

            if match:

                # 不点击必填按钮
                dic['click'] = 0

                # 字段名
                dic['type'] = match.group(1)

            elif not match:
                # 点击必填按钮
                dic['click'] = 1

                # 字段名
                match = re.search(":\s" + "(.*)" + "\s=", s)
                dic['type'] = match.group(1)

            match = re.search("max_length=(\d+),", s)  # 匹配最大长度， 没匹配到就不操作
            if match:
                dic['max_length'] = match.group(1)

            match = re.search("description=\"(\w*)\"", s)  # 描述
            if match:
                dic['desc'] = match.group(1)
            allParameters.append(dic)
            continue

        else:
            dic = {}
            match = re.search("(.*):", s)  # 字段名称
            dic['name'] = match.group(1)
            dic['click'] = 1
            dic['type'] = "object"
            dic['desc'] = "入参"
            allParameters.append(dic)
            continue

    return allParameters