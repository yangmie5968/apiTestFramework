import json


class ReadConfigUTil:
    # 封装读取json文件的方法
    @classmethod
    def read_data(cls, file_path):  # file_path文件路径
        # 读取data.json文件里面的数据
        with open(file_path, "r", encoding="utf8") as f:
            json_data = json.load(f)
        # 定义空列表
        list_data = []
        for i in json_data:
            temp = tuple(i.values())
            list_data.append(temp)
            # 注意：不能for里面return
        return list_data


if __name__ == '__main__':  # 相对路径查看
    # resp = ReadConfigUTil.read_data("../data/ihrm_data.json")
    resp = ReadConfigUTil.read_data("../data/irhm_manage.json")
    print(resp)
