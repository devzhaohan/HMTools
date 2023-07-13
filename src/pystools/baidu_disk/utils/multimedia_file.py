# !/usr/bin/env python3
"""
    xpan multimedia file 
    include:
        listall
        filemetas
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pprint import pprint
from utils.baidu_disk_openapi.api import multimediafile_api
import utils.baidu_disk_openapi as openapi_client
import time


def listall(access_token,path="/",recursion=1,web="1",start=0,limit=2,order="time",desc=1,**kwargs):
    """
    listall
    """
    # Enter a context with an instance of the API client
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = multimediafile_api.MultimediafileApi(api_client)
        access_token = access_token  # str |
        path = path  # str |
        recursion = recursion  # str |
        web = web  # str |  (optional)
        start = start  # int |  (optional)
        limit = limit  # int |  (optional)
        order = order  # str |  (optional)
        desc = desc  # str |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanfilelistall(
                access_token, path, recursion, web=web, start=start, limit=limit, order=order, desc=desc)
            pprint(api_response)
            return api_response
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling MultimediafileApi->xpanfilelistall: %s\n" % e)


def filemetas():
    """
    filemetas
    """
    # Enter a context with an instance of the API client
    with baidu_disk_openapi.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = multimediafile_api.MultimediafileApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        fsids = "[258813175385405]"  # str |
        thumb = "1"  # str |  (optional)
        extra = "1"  # str |  (optional)
        dlink = "1"  # str |  (optional)
        needmedia = 1  # int |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanmultimediafilemetas(
                access_token, fsids, thumb=thumb, extra=extra, dlink=dlink, needmedia=needmedia)
            pprint(api_response)
        except baidu_disk_openapi.ApiException as e:
            print("Exception when calling MultimediafileApi->xpanmultimediafilemetas: %s\n" % e)


if __name__ == '__main__':
    access_token = "126.ed92850b99955145b07017ac21354fa4.Y7dVT8v40Co2b3zsCclgNY7U-dAVENAz4r5rb0D.Uj_d4w"
    listall(access_token,path="/betterme/")
    # filemetas()
