#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

import requests
from hmac import HMAC
from hashlib import sha256
from base64 import b64encode
from .exceptions import DingTlakException
import time
import logging

URL = "https://oapi.dingtalk.com"

_logger = logging.getLogger(__name__)


class Core(object):

    def __get__(self, instance, type):
        self._corpid = instance._corpid
        self._appkey = instance._appkey
        self._appsecret = instance._appsecret
        self._suitticket = instance._suitticket
        self._agentid = instance._agentid
        return self

    def _get_enterprise_access_token(self):
        """
        getting enterprise access token

        :return string: access token
        """
        url = f"{URL}/gettoken"
        res = requests.get(
            url, {"appkey": self._appkey, "appsecret": self._appsecret}).json()
        # 'errcode': 0, 'access_token': 'f0a2837a3412334589cda9c3ab3a93e6', 'errmsg': 'ok', 'expires_in': 7200
        if not res:
            raise Exception()
        return res['access_token']

    def _get_sso_access_token(self):
        """
        getting sso access token

        :return access_token:  sso access token
        """

        url = f"{URL}/sso/gettoken"
        res = requests.get(
            url, {'corpid': self._corpid, 'corpsecret': self._appsecret})
        if not res:
            raise DingTlakException(res)
        return res['access_token']
        

    def _get_corp_access_token(self):
        """
        getting corp access token which auhtorized by app
        """
        url = f"{URL}/service/get_corp_token"
        timestamp = int(time.time())
        res = requests.post(url, data={
            "accessKey": self._appkey,
            "accessSecret": self._appsecret,
            "suiteTicket": self._suitticket,
            "auth_corpid": self._corpid,
            "timestamp": timestamp,
            "signature": self._sign_corp_request(timestamp)
        })
        return res

    def _sign_corp_request(self, timestamp):
        """
        compute signature for third app request.
        """
        signstring = f"{timestamp}\n{self._suitticket}"
        return b64encode(HMAC(self._appsecret, signstring, sha256).digest())

    def _post(self, url, data):
        try:
            # [FIXME] other two type requests
            access_token = self._get_enterprise_access_token()
            res = requests.post(
                f"{url}?access_token={access_token}", json=data).json()
            if res['errcode'] != 0:
                _logger.debug(f"[DingTalk Request]:{data}")
                raise DingTlakException(**res)
            return res
        except Exception as err:
            raise Exception(err)
