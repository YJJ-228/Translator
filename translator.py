#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import os

import selecting_clipboard as scl

appid = '20240125001950970'  # 填写你的appid
secretKey = 'b_M2VbGARlvXVhcjKZ_O'  # 填写你的密钥

def translating(q):
    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    # toLang = 'en'   #译文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['trans_result'][0]['dst']

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

if __name__=='__main__':
    os.system("echo off|clip")
    os.system("echo on")
    last_selected_text = ""
    while True:
        selected_text = scl.get_selected_text()
        if selected_text != last_selected_text:
            last_selected_text = selected_text
            ans=translating(selected_text)
            print(ans)
    