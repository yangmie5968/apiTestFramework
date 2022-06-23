import requests


# 使用类对象可以直接调用
class IHRMManageApi(object):
    # 返回添加员工接口
    @classmethod
    def add_emp_api(cls, token, json_data):
        url = "http://ihrm-test.itheima.net/api/sys/user"
        header = {"Content-Type": "application/json", "Authorization": token}
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp

    # 返回查询员工接口
    @classmethod
    def query_emp_api(cls, emp_id, token):
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        header = {"Content-Type": "application/json",
                  "Authorization": token}
        resp = requests.get(url=url, headers=header)
        return resp

    #  返回修改员工接口
    @classmethod
    def modify_emp_api(cls, emp_id, token, json_data):
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        header = {"Content-Type": "application/json",
                  "Authorization": token}
        modify_resp = requests.get(url=url, headers=header, json=json_data)
        return modify_resp

    #  返回删除员工接口
    @classmethod
    def del_emp_api(cls, emp_id, token):
        delete_url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        add_emp_headers = {"Content-Type": "application/json",
                           "Authorization": token}
        delete_resp = requests.get(url=delete_url, headers=add_emp_headers)
        return delete_resp
