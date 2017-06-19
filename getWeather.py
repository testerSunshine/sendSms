# -*- coding: utf8 -*-
import json
from time import sleep
import myUrllib


class Weather(object):
    def __init__(self, city_name):
        self.city_name = city_name
        self.weatherInfo = dict()
        self.message = []

    def __str__(self):
        return " ".join(self.message)

    def getMessage(self):
        return self.message

    def getWeatherInfo(self):
        for i in range(520):
            self.weatherUrl = "http://www.sojson.com/open/api/weather/json.shtml?city={}".format(self.city_name)
            result = json.loads(myUrllib.get(self.weatherUrl))
            if "status" in result and result["status"] is 200 and result["data"]:
                self.weatherInfo = result["data"]["forecast"][0]   # 获取今日天气预报
                break
            else:
                print(result["status"])
            sleep(1)

    def sendMessageByTemperature(self):
        self.message.append("新的一天又来啦，给小主念早安早安早安，重要的事情说三遍，今天是{}".format(self.weatherInfo["date"]))
        self.message.append("%s最高温度 %s，最低温度 %s" % (self.city_name, self.weatherInfo["high"].split(" ")[1], self.weatherInfo["low"].split(" ")[1]))

    def sendMessageByType(self):
        if self.weatherInfo["type"] == "晴" or self.weatherInfo["type"] == "晴转多云" or self.weatherInfo["type"] == "多云":
            self.message.append("天气是:{}，看起来很好，想和小主约一下".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "阴":
            self.message.append("天气是:{}，天气一般，小主呆在家里好好追剧最好".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "雾":
            self.message.append("天气是:{}，出门眼睛要擦亮哦，小主要看好老公！".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "雨夹雪":
            self.message.append("天气是:{}，把伞带好，小主还是别出门啦，如果硬要出，把家里的皮大衣拿来".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "雷阵雨" or self.weatherInfo["type"] == "小雨" or self.weatherInfo["type"] == "大雨" or self.weatherInfo["type"] == "中雨" or self.weatherInfo["type"] == "雨":
            self.message.append("天气是:{}，把伞伞伞带好，重要的事情说三遍，下班自当来接小主回家哦！".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "暴雨":
            self.message.append("天气是:{}，今天要不出去了，太可怕了！".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "大雪" or self.weatherInfo["type"] == "小雪" or self.weatherInfo["type"] == "中雪":
            self.message.append("天气是:{}，呆在家里多暖和，起什么床呀！来呀，快活啊，反正有大把时光！".format(self.weatherInfo["type"]))
        elif self.weatherInfo["type"] == "冰雹":
            self.message.append("天气是:{}，安全第一，在家好好呆着，文大帅冒死也会给小主弄吃的".format(self.weatherInfo["type"]))

    def sendMessageByWantTosay(self):
        pass

    def main(self):
        self.getWeatherInfo()
        self.sendMessageByTemperature()
        self.sendMessageByType()
        return "".join(self.message)

if __name__ == '__main__':
    w = Weather("长沙")
    print(w.main())
