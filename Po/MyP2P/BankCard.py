from Libs.business import LoginClass

class BankCardApi(LoginClass):
    # 绑定银行卡业务
    def bindBankCard(self):

        # 纵向继承关系所以可以调用登录接口
        # 登录登录接口成功后cookies的字典数据会被更新
        self.loginApi()

        # 绑定数据接口的path
        bind_path = '/member.php?ctl=uc_money&act=savebank'

        # 绑定数据接口的数据
        bind_data = {
            'real_name': 'liudehua',
            'bank_id': '2',
            'otherbank': '',
            'region_lv1': '1',
            'region_lv2': '4',
            'region_lv3': '57',
            'region_lv4': '559',
            'bankzone': 'aaaa',
            'bankcard': '1234 5678 903',
            'reBankcard': '1234 5678 903'
        }

        # 发送请求
        # self.cookies的数据是从登录类中获得的
        res = self.httpSend(path=bind_path,data=bind_data,cookies=self.cookies)
        return res