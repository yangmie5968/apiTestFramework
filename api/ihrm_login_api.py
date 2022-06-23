import requests


class IHRMLoginAPI(object):
    # 登录接口
    @classmethod
    def ihrm_login_api(cls, data):
        url = " http://ihrm-test.itheima.net/api/sys/login"
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url=url, headers=headers, json=data)
        return resp
