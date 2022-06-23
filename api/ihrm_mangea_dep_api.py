import requests


class IHRMMangDEPApi(object):
    # 添加部门
    @classmethod
    def add_dep_api(cls, token, data):
        url = "http://ihrm-test.itheima.net/api/company/department"
        header = {'Content-Type': 'application/json', 'Authorization': token}
        resp = requests.post(url=url, headers=header, json=data)
        return resp

    # 查询部门
    @classmethod
    def query_dep_api(self, dep_id, token):
        url = "http://ihrm-test.itheima.net/api/company/department/" + dep_id
        header = {'Authorization': token}
        resp = requests.get(url=url, headers=header)
        return resp

    # 修改部门
    @classmethod
    def modify_dep_api(self, dep_id, token, data):
        url = "http://ihrm-test.itheima.net/api/company/department/" + dep_id
        header = {'Content-Type': 'application/json', 'Authorization': token}
        resp = requests.put(url=url, headers=header, json=data)
        return resp

    # 删除部门
    @classmethod
    def del_dep_api(self, dep_id, token):
        url = "http://ihrm-test.itheima.net/api/company/department/" + dep_id
        header = {'Authorization': token}
        resp = requests.delete(url=url, headers=header)
        return resp
