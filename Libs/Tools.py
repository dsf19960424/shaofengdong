# 公共模块
import requests
import unittest
class BaseHttp(object):
    host = 'http://localhost'

    # 统一http发送方式
    def httpSend( self,path,method='post', **kwargs):
        # 拼接请求url，host的数据在类变量中
        url = '{}{}'.format(self.host, path)
        res = requests.request(url=url,method=method, **kwargs)
        return res

# 统一封装校验类
class VerifyClass(unittest.TestCase):
    # 检验状态码
    # 校验json格式响应体
    # text/html格式响应体
    # 检验响应体的特殊字段

    # 通用调用一个方法，去校验接口的多样性
    def verify_json_data(self, target, key, result_data):
        '''
        :param target: 未处理的接口响应
        :param key: 需要获取响应的Key
        :param result_data: 检验的字段
        :return:
        '''
        code = target.status_code
        target = target.json()
        self.assertEqual(200, code)
        self.assertEqual(target.get(key), result_data)

    def verify_html_data(self, target, result_data):
        code = target.status_code
        target = target.text
        self.assertEqual(200, code)
        self.assertIn(result_data, target)