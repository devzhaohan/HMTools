# !/usr/bin/env python3
"""
    xpan auth
    include:
        authorization_code, just get token by code
        refresh_token
        device_code
"""
import os,sys

from .baidu_disk_openapi.api import auth_api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# from baidu_disk_openapi.api import auth_api
from pprint import pprint


def oauthtoken_authorizationcode():
    """
    authorizationcode
    get token by authorization code
    """
    # Enter a context with an instance of the API client
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        code = "3ce3370c960ce929306c419d32f92df1" # str |
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str |
        client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str |

        redirect_uri = "oob" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_code2token(code, client_id, client_secret, redirect_uri)
            pprint(api_response)
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_code2token: %s\n" % e)


def oauthtoken_refreshtoken():
    """
    refresh access token
    """
    # Enter a context with an instance of the API client
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        refresh_token = "122.5d587a6620cf03ebd221374097d5342a.Y3l9RzmaC4A1xq2F4xQtCnhIb4Ecp0citCARk0T.Uk3m_w" # str | 
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_refresh_token(refresh_token, client_id, client_secret)
            pprint(api_response)
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_refresh_token: %s\n" % e)


def oauthtoken_devicecode():
    """
    devicecode 
    get device code 
    """
    # Enter a context with an instance of the API client
    configuration = baidu_disk_openapi.Configuration()
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        scope = "basic,netdisk" # str |
        client_id = Config['BaiduYunpan'][Tenant.PMZHAO][ 'app_key']


        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_device_code(client_id, scope)
            # pprint(api_response)
            return api_response
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_device_code: %s\n" % e)


def oauthtoken_devicetoken(code):
    """
    get token by device code
    """
# Enter a context with an instance of the API client
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        # code = "1dc8cf189c863f094d25843dbbd3f633" # str |
        # client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str |
        # client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str |
        client_id = Config['BaiduYunpan'][Tenant.PMZHAO][ 'app_key']
        client_secret = Config['BaiduYunpan'][Tenant.PMZHAO][ 'secret_key']

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_device_token(code, client_id, client_secret)
            pprint(api_response)
            return api_response
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_device_token: %s\n" % e)

def auth_from_qr():

    # 1.扫码登录
    res1 = oauthtoken_devicecode()
    print(res1)
    # {'device_code': '0993010f33712ad7ff2de4ff76db2f2e',
    #  'expires_in': 300,
    #  'interval': 5,
    #  'qrcode_url': 'https://openapi.baidu.com/device/qrcode/6ad8f3eb08e1f9ceb1e3d9958c6e9807/bhaq4ptd',
    #  'user_code': 'bhaq4ptd',
    #  'verification_url': 'https://openapi.baidu.com/device'}

    qr_url = res1["qrcode_url"]
    # 展示二维码
    print(qr_url)

    # 提示用户扫码，等待输入y继续后面的操作
    input("请扫码登录后，输入y继续：")

    device_code = res1["device_code"]
    res2 = oauthtoken_devicetoken(res1["device_code"])

def auth_from_url():
    pass

if __name__ == '__main__':
    """
    main
    """

    auth_from_qr()

    # oauthtoken_authorizationcode()
    # oauthtoken_refreshtoken()

    # # 简化授权
    # resq_id = SEncoder.short_uuid()
    # redirect_uri = "oob"  # str |
    # client_id = Config['BaiduYunpan'][Tenant.PMZHAO][ 'app_key']
    # user_url = "http://openapi.baidu.com/oauth/2.0/authorize?response_type=token&"\
    #             f"client_id={client_id}&"\
    #             f"redirect_uri={redirect_uri}&"\
    #             "scope=basic,netdisk&" \
    #            "display=page&" \
    #            f"state={resq_id}" \
    #
    #
    #
    # print(user_url)
    # input("请先打开页面授权，输入y继续：")





