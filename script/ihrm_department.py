from api.ihrm_mangea_dep_api import IHRMMangDEPApi
from common.assert_util import AssertUtil
from common.dep_id_util import DepIDUtil
from common.token_util import TokenUtil


class TestIHRMdep(object):
    def setup_class(self):
        # teoken 有时效形,不用每个测试方法前执行一次,
        # 整个类对象调用一次执行一次就行
        self.token = TokenUtil.get_token()

    # 添加部门
    def test_add_dep(self):
        data = {"name": "测试部门999", "code": "123789"}
        resp = IHRMMangDEPApi.add_dep_api(self.token, data)
        AssertUtil.ihrm_assert(resp, 200, True, 10000, "操作成功！")

    # 查询部门
    def test_query_dep(self):
        resp = IHRMMangDEPApi.query_dep_api(DepIDUtil.get_dep_id(), self.token)
        AssertUtil.ihrm_assert(resp, 200, True, 10000, "操作成功！")

    # 修改部门
    def test_modify_dep(self):
        dep_id = DepIDUtil.get_dep_id()
        data = {"name": "测试部门58", "code": "125289"}
        resp = IHRMMangDEPApi.modify_dep_api(dep_id, self.token, data)
        AssertUtil.ihrm_assert(resp, 200, True, 10000, "操作成功！")

    # 删除部门
    def test_del_dep(self):
        dep_id = DepIDUtil.get_dep_id()
        resp = IHRMMangDEPApi.del_dep_api(dep_id, self.token)
        AssertUtil.ihrm_assert(resp, 200, True, 10000, "操作成功！")


