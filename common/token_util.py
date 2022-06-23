import requests


class TokenUtil:
    # 封装读取令牌token的方法
    @classmethod
    def get_token(cls):
        url = " http://ihrm-test.itheima.net/api/sys/login"
        headers = {"Content-Type": "application/json"}
        data = {"mobile": "13800000002", "password": "123456"}
        resp = requests.post(url=url, headers=headers, json=data)
        token = resp.json().get("data")
        return token

    # @classmethod
    # def add_emp_api(cls, token):
    #     url = "http://ihrm-test.itheima.net/api/sys/user"
    #     header = {"Content-Type": "application/json", "Authorization": token}
    #     json_data = {
    #         "username": "我是老6",
    #         "mobile": "17612535994",
    #         "workNumber": "22"}
    #     resp = requests.post(url=url, headers=header, json=json_data)
    #     resp.json().get('data').get('id')
    #     print(resp)

    # 封装读取查询员工的方法

