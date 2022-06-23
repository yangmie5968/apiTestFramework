from api.ihrm_login_api import IHRMLoginAPI
from common.assert_util import AssertUtil


class TestIHRMLogin(object):
    # 登录成功
    def test_login_success(self):
        data = {"mobile": "13800000002", "password": "123456"}
        resp = IHRMLoginAPI.ihrm_login_api(data)
        AssertUtil.ihrm_assert(resp, 200, True, 10000, '操作成功！')

    # 手机号错误
    def test_mobile_error(self):
        data = {"mobile": "1380000000", "password": "123456"}
        resp = IHRMLoginAPI.ihrm_login_api(data)
        AssertUtil.ihrm_assert(resp, 200, False, 20001, '用户名或密码错误')

    # 密码错误
    def test_password_error(self):
        data = {"mobile": "13800000002", "password": "13456"}
        resp = IHRMLoginAPI.ihrm_login_api(data)
        AssertUtil.ihrm_assert(resp, 200, False, 20001, '用户名或密码错误')
