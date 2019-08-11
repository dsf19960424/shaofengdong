from Libs.Tools import BaseHttp

# 公共业务登录类继承了BaseHttp
class LoginClass(BaseHttp):
    # 定义一个空的字典数据
    cookies = {
        'PHPSESSID': ''
    }

    def loginApi(self):
        # 登录接口
        lgn_path = '/index.php?ctl=user&act=dologin'
        # 登录数据
        lgn_data = {
            'email': 'dong66661145',
            'user_pwd':
                'Q0tPS1VUdWthenRuT1JRTll5TEJFeERkeVB1SWhjYnBZZ3hKeFJSbG1nd1d5TVNGSHolMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTQxMTY1JTI1dThGNkYlMjV1NEVGNg==',
            'ajax': 1
        }
        # 发送登录请求
        lgn_res = self.httpSend(path=lgn_path, data=lgn_data)

        # 发送登录请求
        pipid = lgn_res.cookies['PHPSESSID']

        # 为上面的类变量cookies更新其数据
        self.cookies['PHPSESSID'] = pipid

        return lgn_res