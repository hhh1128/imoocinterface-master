#coding = utf-8
import sys
import os
import configparser

from Tools.scripts.generate_opcode_h import header

base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json


class BaseRequest:
    def send_post(self,url,data,cookie=None,get_cookie=None,headers=None):
        '''
        发送post请求
        '''

        reponse = requests.post(url=url,data=data,cookies=cookie,headers=headers)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''