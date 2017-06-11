# -*- coding: utf8 -*-
import myUrllib

class SendMessage(object):
    def __init__(self, phone, params):
        self.phone = phone
        self.params = params
        self.APPKEY = "50792ac04a966ce8be51ccbbf55964c2"
        self.AppSecret = "77363f51c135"

    def send(self):
        sendUrl = "'https://api.netease.im/sms/sendtemplate.action"
