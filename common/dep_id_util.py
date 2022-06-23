from api.ihrm_mangea_dep_api import IHRMMangDEPApi
from common.token_util import TokenUtil


class DepIDUtil:
    # 添加员工的部门id
    @classmethod
    def get_dep_id(cls):
        data = {"name": "测试部门999", "code": "123789"}
        token = TokenUtil.get_token()
        resp = IHRMMangDEPApi.add_dep_api(token, data)
        dep_id = resp.json().get("data").get("id")
        return dep_id


if __name__ == '__main__':
    resp= DepIDUtil.get_dep_id()
    print(resp)
