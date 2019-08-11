import unittest
from Libs.Tools import VerifyClass
from Po.MyP2P.BankCard import BankCardApi

class TestBankCard(unittest.TestCase):
    def setUp(self):
        # 实例化绑定银行卡类
        self.bc = BankCardApi()

    def test001(self):
        # 发送银行卡请求
        res = self.bc.bindBankCard()
        # 校验字典中包含的值是否存在
        self.verify_json_data(res, 'info', '保存成功')

    def test002(self):
        # 发送银行卡请求
        res = self.bc.bindBankCard()
        self.verify_json_data(res, 'info', '该银行卡已存在')

if __name__ == '__main__':
    unittest.main(verbosity=2)