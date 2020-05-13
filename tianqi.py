#!/usr/bin/python3
# -*- coding: UTF-8 -*-s

"""导入模块"""
import urllib
import json
import sys
import os
import time
import signal

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode


# """  获取今天的天气信息并生成接口   """ 
def getWeatherDetail():
    WEATHER_CODE = {
        "00": "晴",
        "01": "多云",
        "02": "阴",
        "03": "阵雨",
        "04": "雷阵雨",
        "05": "雷阵雨伴有冰雹",
        "06": "雨夹雪",
        "07": "小雨",
        "08": "中雨",
        "09": "大雨",
        "10": "暴雨",
        "11": "大暴雨",
        "12": "特大暴雨",
        "13": "阵雪",
        "14": "小雪",
        "15": "中雪",
        "16": "大雪",
        "17": "暴雪",
        "18": "雾",
        "19": "冻雨",
        "20": "沙尘暴",
        "21": "小到中雨",
        "22": "中到大雨",
        "23": "大到暴雨",
        "24": "暴雨到大暴雨",
        "25": "大暴雨到特大暴雨",
        "26": "小到中雪",
        "27": "中到大雪",
        "28": "大到暴雪",
        "29": "浮尘",
        "30": "扬沙",
        "31": "强沙尘暴",
        "53": "霾",
        "99": ""
    }
    url = 'https://weatherapi.market.xiaomi.com/wtr-v3/weather/all?latitude=110&longitude=112&isLocated=true&locationKey=weathercn%3A101270106&days=1&appKey=weather20151024&sign=zUFJoAR2ZVrDy1vF3D07&romVersion=7.2.16&appVersion=87&alpha=false&isGlobal=false&device=cancro&modDevice=&locale=zh_cn'
    json_data = res = urlopen(url)
    parsed_weather = json.loads(json_data.read())
    temperature = parsed_weather['current']['temperature']['value']
    humidity = parsed_weather['current']['humidity']['value']
    today_forecast = parsed_weather['forecastDaily']['weather']['value'][
        0
    ]
    weather_from = '%02d' % (int(today_forecast['from']))
    weather_from = WEATHER_CODE[weather_from]
    weather_to = '%02d' % (int(today_forecast['to']))
    weather_to = WEATHER_CODE[weather_to]
    temperature_from = parsed_weather['forecastDaily']['temperature'][
        'value'
    ][0]['from']
    temperature_to = parsed_weather['forecastDaily']['temperature'][
        'value'
    ][0]['to']
    weather_detail = "尊敬的凯文, 您好, 我是您的天气助手, 小白龙。接下来将为您播报今天的天气预报信息, 目前温度{0}度,相对湿度{1}%,今天天气{2}转{3},温度{4}度到{5}度".format(
            temperature, humidity, weather_from, weather_to,
            temperature_from, temperature_to)
    return weather_detail


# """  获取百度云文字转语音接口的access_token   """
"""  TOKEN start """
def fetch_token():
    
    API_KEY = 'kVcnfD9iW2XVZSMaLMrtLYIz'
    SECRET_KEY = 'O9o1O213UgG5LFn0bDGNtoRN3VWl2du6'
    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
    IS_PY3 = 3

    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)
    return result['access_token']
"""  TOKEN end """


# """  Unix Mac python播放器类库  """
"""播放音乐开始"""
def palyMusic():

    import wave
    import pyaudio

    CHUNK = 1024

    wf = wave.open('/Users/kevinfei/Documents/python/天气播报/text2audio.wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while data != '':
        if data == b'':
            os.kill(os.getpid(), signal.SIGKILL)
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()    
"""播放音乐结束"""


# """ 开始播报天气信息 """
def getText2Audio(access_token):
    weather_detail = getWeatherDetail()
    audioUrl = 'http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=mypi&tok=' + access_token + '&tex=%s&vol=9&per=111&aue=6' % urllib.request.quote(weather_detail)
    print(audioUrl)
    response = urlopen(audioUrl)
    html     = response.read()
    with open('/Users/kevinfei/Documents/python/天气播报/text2audio.wav', 'wb') as f:  # 用wb模式打开创建文件，w写模式
        f.write(html)  # 写入二进制文件内容
   

getText2Audio(fetch_token())

palyMusic()