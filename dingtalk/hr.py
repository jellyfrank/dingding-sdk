#!/usr/bin/python3
# @Time    : 2021-06-28
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


class HR(Core):

    def get_official_employees(self, status=None, offset=0, size=50):
        """
        get official employees

        :param status: official status: 2 trial, 3. official, 5 dimission, -1 no status
        :param offset: offset
        :param size: page size

        :return result: {'next_cursor':xx, 'data_list': list of user id.} no next_cursor means ending of result.
        """

        url = "{URL}/topapi/smartwork/hrm/employee/queryonjob"
        data = {
            'status_list': status,
            'offset': offset,
            'size': size
        }
        res = self._post(url, data)
        return res['result']

    def get_candidates(self, offset=0, size=50):
        """
        get candidates who is going to be official.

        :param offset: offset
        :param size: size 

        :return result: {'next_cursor':xx, 'data_list': list of user id.} no next_cursor means ending of result.
        """
        url = "{URL}/smartwork/hrm/employee/querypreentry"
        data = {
            'offset': offset,
            'size': size
        }
        res = self._post(url, data)
        return res['result']
