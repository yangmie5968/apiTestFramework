class AssertUtil:

    # 封装断言的方法 TP商城
    @classmethod
    def tpshop_assert(cls, resp, status_code, status, msg):
        assert resp.status_code == status_code
        assert resp.json().get("status") == status
        assert resp.json().get("mag") == msg

    # 封装断言的方法 人力资源
    @classmethod
    def ihrm_assert(cls, resp, status_code, success, code, message):
        assert resp.status_code == status_code
        assert resp.json().get('success') == success
        assert resp.json().get('code') == code
        assert resp.json().get('message') == message

