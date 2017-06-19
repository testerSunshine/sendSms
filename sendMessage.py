# -*- coding: utf8 -*-
import os
import urllib2
from time import sleep

import yaml
import myUrllib
from getWeather import Weather


class sendMessage(object):
    def __init__(self):
        self.smsAgrs = self._get_yaml()["sms"]
        self.weather = self._get_yaml()["Weather"]
        self.phone = self.smsAgrs["phone"]
        self.name = self.smsAgrs["name"]
        self.pwd = self.smsAgrs["pwd"]
        self.sign = self.smsAgrs["sign"]

    def _getBalance(self):
        """
        获取余额
        :return:1 代表 余额不足  0 代表余额充足
        """
        sendUrl = "http://web.cr6868.com/asmx/smsservice.aspx?name={}&pwd={}&type=balance".format(self.name, self.pwd)
        resultB = myUrllib.get(sendUrl)
        if resultB is not None:
            spResultB = resultB.split(",")
            code = spResultB[0]
            banlance = int(spResultB[1])
            if code == "0" and banlance > 0:
                print("当前短信剩余条数：{}".format(str(banlance)))
                return 0
        else:
            return 1

    def _sendInfo(self, content, phone):
        """
        发送短信内容
        :return: 0 代表发送成功 1 代表发送失败
        """
        content = content.encode("utf-8")
        content = urllib2.quote(content)
        sendUrl = "http://web.cr6868.com/asmx/smsservice.aspx?name={}&pwd={}&content={}&mobile={}&stime=&sign={}&type=pt&extno=".format(self.name, self.pwd, content, phone, self.sign)
        # sendUrl = "http://web.cr6868.com/asmx/smsservice.aspx"
        # data = {
        #     "name": self.name,
        #     "pwd": self.pwd,
        #     "content": content,
        #     "mobile": self.phone,
        #     "sign": self.sign,
        # }
        infoResult = myUrllib.get(sendUrl)
        if infoResult is not None:
            code = infoResult.split(",")[0]
            if int(code) == 0:
                return 0
            elif int(code) == 1:
                print("当前短信发送失败，含有铭感词汇，短信内容为：{}".format(content))
                return 1
        else:
            print("接口返回值为空")

    def _get_yaml(self):
        """
        解析yaml
        :return: s  字典
        """
        path = os.path.join(os.path.dirname(__file__) + '/conf.yaml')
        f = open(path)
        s = yaml.load(f)
        f.close()
        if s is not None:
            return s
        else:
            print("conf content is None")

    def main(self):
        balance = self._getBalance()
        if int(balance) == 0:
            for i in range(len(self.phone)):
                content = Weather(self.weather["city_name"][i]).main()
                status = self._sendInfo(content, self.phone[i])
                if status == 0:
                    print("当前短信发送成功，发送的手机号为：{} 发送内容为：{}".format(self.phone[i], content))
                else:
                    print("当前短信发送失败，可能有敏感字符，发送内容为：{}".format(content))
                sleep(1)
        elif int(balance) == 1:
            print("余额不足")

if __name__ == '__main__':
    s = sendMessage()
    s.main()