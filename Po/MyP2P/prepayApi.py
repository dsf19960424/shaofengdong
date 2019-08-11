from Libs.Tools import httpSend

def perpayApi(cookies):
    lgn_cookies = {
        'PHPSESSID': '{}'.format(cookies)
    }
    # 支付接口 线下支付
    perpay_path = '/member.php?ctl=uc_money&act=incharge_done'
    # 支付数据
    prepay_data = {
        'check_ol_bl_pay': 'on',
        'money': '5551',
        'pingzheng': '',
        'memo': '777771',
        'payment': '5',
        'bank_id': '0',
    }
    # 调用封装好的发送请求方法
    prepay_res = httpSend(method='post', path=perpay_path, data=prepay_data, cookies=lgn_cookies)
    return prepay_res
