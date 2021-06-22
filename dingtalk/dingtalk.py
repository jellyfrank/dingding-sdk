#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core
from .contact import Department, Role, User


class DingTalk(object):

    def __init__(self, corpid, appkey, appsecret, suitticket=None):
        """
        init dingtalk client

        params:
        corpid: Corpration Id
        appkey: app key
        appsecret: app secret
        suitticket: suit ticket from dingtalk when using third party app.
        """
        self._corpid = corpid
        self._appkey = appkey
        self._appsecret = appsecret
        self._suitticket = suitticket

    core = Core()
    department = Department()
    role = Role()
    user = User()

    # def _get_enterprise_access_token(self):
    #     """
    #     getting enterprise access token.
    #     """
    #     url =
