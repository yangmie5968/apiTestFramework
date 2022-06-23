import config  # 导入绝对路径
from api.ihrm_manage_emp import IHRMManageApi  # 导入接口
from common.assert_util import AssertUtil  # 导入断言
from common.irhm_mysql_util import DBUtil  # 导入数据库
from common.read_config_util import ReadConfigUTil  # 转换json文件
from parameterized import parameterized  # 导入参数化
from common.token_util import TokenUtil  # 导入登录接口


class TestIHRMManageEMP(object):
    # 定义文件路径
    ihrm_login_file = config.BASE_DIR + "/data/irhm_manage.json"

    # 所有的测试用例执行前，执行一次即可，token 一般过30分钟后才到期
    def setup_class(self):
        self.token = TokenUtil.get_token()

    # 执行测试用例前，从数据库删除手机号记录
    def setup(self):
        del_sql = f"DELETE from bs_user where mobile = '{config.TEL}';"
        DBUtil.uid_db(del_sql)

    # 测试用例执行完后，从数据库删除手机号记录，避免生成脏数据
    def teardown(self):
        del_sql = f"DELETE  from bs_user where mobile = '{config.TEL}';"
        DBUtil.uid_db(del_sql)

    @parameterized.expand(ReadConfigUTil.read_data(ihrm_login_file))
    def test_add_emp(self, body, status_code, success, code, message):
        resp = IHRMManageApi.add_emp_api(self.token, body)
        AssertUtil.ihrm_assert(resp, status_code, success, code, message)

    def query_emp(self):
        pass