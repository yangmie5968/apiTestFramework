
import config  # 导入绝对路径
from api.ihrm_login_api import IHRMLoginAPI  # 导入测试接口
from common.assert_util import AssertUtil  # 导入断言
from parameterized import parameterized  # 导入参数化
from common.read_config_util import ReadConfigUTil  # 转换json文件


class TestIHRMLogin(object):
    # 定义login_data的绝对路径
    ihrm_login_file_path = config.BASE_DIR + "/data/ihrm_data.json"

    # 测试登录接口手机号正确,手机号已注册,密码错误
    @parameterized.expand(ReadConfigUTil.read_data(ihrm_login_file_path))
    def test_login_success(self, body, status_code, success, code, message):
        resp = IHRMLoginAPI.ihrm_login_api(body)
        AssertUtil.ihrm_assert(resp, status_code, success, code, message)
